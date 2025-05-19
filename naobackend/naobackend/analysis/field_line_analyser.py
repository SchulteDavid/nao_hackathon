import numpy as np  # linear algebra
import cv2
import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt
import numpy as np
import shapely
from shapely.ops import unary_union
from shapely.geometry import LineString
from shapely.ops import linemerge
from statistics import mean, median

from shapely.geometry import LineString


class FieldLineAnalyser:
    def __init__(self):
        self.images_path = f'../../images/field_lines/'

        # Parse the XML file
        xml_file = '/home/felixl/nao/nao_hackathon/data/field_lines/annotations.xml'
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

        self.buffer_size = 5

    # Function to parse points from a string
    @staticmethod
    def parse_points(points_str):
        points = []
        for point in points_str.split(';'):
            x, y = point.split(',')
            points.append((float(x), float(y)))
        points = np.array(points, dtype=np.int32)
        return points
    @staticmethod
    def plot_polygon(poly, img, line_color=(0, 255, 0), line_thickness=2):
        # Get the exterior coordinates of the polygon
        exterior_coords = np.array(poly.exterior.coords).astype(int)

        # Draw the polygon on the image
        cv2.polylines(img, [exterior_coords], isClosed=True, color=line_color, thickness=line_thickness)

    def plot_img(self, element, image):

        for polygon in element.iter('polygon'):
            str_point = polygon.get('points')
            pointss = self.parse_points(str_point)
            pointss = np.append(pointss, [pointss[0]], axis=0)
            for point_idx, ele in np.ndenumerate(pointss):
                point_idx = point_idx[0]
                self.plot_polygon(
                    LineString([pointss[point_idx], pointss[(point_idx + 1) % len(pointss)]]).buffer(self.buffer_size + 4),
                    image, line_thickness=1)

        for line in element.iter('line'):
            str_point = line.get('points')
            pointss = self.parse_points(str_point)
            # draw the line on the image
            cv2.line(image, tuple(pointss[0]), tuple(pointss[1]), (0, 0, 255), 2)

        print(element.attrib['name'])

        return image

    def calc_metrics(self, labels, prediction):
        ground_truth = []
        detector_output = []
        iou = 0

        for line_element in prediction:
            points_str = line_element['points']
            points = self.parse_points(points_str)
            detector_output.append(LineString(points).buffer(self.buffer_size))

        for polygon_element in labels.iter('polygon'):
            points_str = polygon_element.get('points')
            points = self.parse_points(points_str)
            points = np.append(points, [points[0]], axis=0)
            for point_idx, ele in np.ndenumerate(points):
                point_idx = point_idx[0]
                ground_truth.append(
                    LineString([points[point_idx], points[(point_idx + 1) % len(points)]]).buffer(self.buffer_size))

        union_all_poly = unary_union(ground_truth)
        union_all_line = unary_union(detector_output)

        intersection = union_all_poly.intersection(union_all_line)

        union = union_all_poly.union(union_all_line)

        iou = intersection.area / union.area

        # calculate false positives area
        # get the area where the detector output is not in the ground truth
        diff = self.calc_false_positives(labels, prediction)

        return diff, iou

    def calc_false_positives(self, labels, prediction):
        ground_truth = []
        detector_output = []

        for line_element in prediction:
            points_str = line_element['points']
            points = self.parse_points(points_str)
            detector_output.append(LineString(points))

        for polygon_element in labels.iter('polygon'):
            points_str = polygon_element.get('points')
            points = self.parse_points(points_str)
            points = np.append(points, [points[0]], axis=0)
            for point_idx, ele in np.ndenumerate(points):
                point_idx = point_idx[0]
                ground_truth.append(
                    LineString([points[point_idx], points[(point_idx + 1) % len(points)]]).buffer(self.buffer_size + 4))

        # calculate the lenght of the detector_output lines that are not in the ground_truth polygons
        diff = unary_union(detector_output).difference(unary_union(ground_truth))

        return diff.length

    # a function that calculates the true_positives for a given element
    def calc_true_positives(self, labels, prediction):
        ground_truth = []
        detector_output = []

        for line_element in prediction:
            points_str = line_element['points']
            points = self.parse_points(points_str)
            detector_output.append(LineString(points))

        for polygon_element in labels.iter('polygon'):
            points_str = polygon_element.get('points')
            points = self.parse_points(points_str)
            points = np.append(points, [points[0]], axis=0)
            for point_idx, ele in np.ndenumerate(points):
                point_idx = point_idx[0]
                ground_truth.append(
                    LineString([points[point_idx], points[(point_idx + 1) % len(points)]]).buffer(self.buffer_size + 4))

        # calculate the lenght of the detector_output lines that are in the ground_truth polygons
        intersection = unary_union(detector_output).intersection(unary_union(ground_truth))

        return intersection.length

    # a function to calculate the false negatives
    def calc_false_negatives(self, label, prediction):
        ground_truth = []
        detector_output = []

        for line_element in prediction:
            points_str = line_element.get('points')
            points = self.parse_points(points_str)
            detector_output.append(LineString(points))

        for polygon_element in label.iter('polygon'):
            points_str = polygon_element.get('points')
            points = self.parse_points(points_str)
            points = np.append(points, [points[0]], axis=0)
            for point_idx, ele in np.ndenumerate(points):
                point_idx = point_idx[0]
                ground_truth.append(
                    LineString([points[point_idx], points[(point_idx + 1) % len(points)]]).buffer(self.buffer_size + 4))

        # calculate the length of the ground_truth polygons that are not in the detector_output lines
        diff = unary_union(ground_truth).difference(unary_union(detector_output))

        return diff.length

    def calc_metrics_for_all_images(self, detection_function):
        iou_array = []
        true_positives = 0
        false_positives = 0
        false_negatives = 0

        labels = self.root

        for label in self.root.iter('image'):
            image_name = label.get('name')

            #load image
            image = cv2.imread(self.images_path + image_name)

            #predict
            prediction = detection_function(image)

            false_positive, iou = self.calc_metrics(label, prediction)
            iou_array.append(iou)

            false_positives += false_positive

            true_positive = self.calc_true_positives(label, prediction)
            true_positives += true_positive

            false_negative = self.calc_false_negatives(label, prediction)
            false_negatives += false_negative

            recall = true_positive / (true_positive + false_negative)
            if true_positive + false_positive == 0:
                precision = 0
            else:
                precision = true_positive / (true_positive + false_positive)

        # calculate the precision
        precision = true_positives / (true_positives + false_positives)
        # calulate recall
        recall = true_positives / (true_positives + false_negatives)

        # calculate f1 score with more weight on precision
        beta = 0.5
        f1 = (1 + beta ** 2) * (precision * recall) / ((beta ** 2 * precision) + recall)

        return precision, recall, iou_array, f1
