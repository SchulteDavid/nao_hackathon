import cv2
import os
import sys
import numpy as np
import random
import hashlib

file_endings = set([
    "jpg",
    "jpeg",
    "png",
    "gif"
])

try:
    annotated_images = set([l.strip() for l in open("annotated_images.txt").readlines()])
except FileNotFoundError:
    annotated_images = set()

class_colors = {
    "ball": (255, 255, 0),
}

class_ids = {
    "ball": 0,
}

images = []
for path, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        ending = f.split('.')[-1]
        if ending in file_endings:
            full_path = os.path.abspath(os.path.join(path, f))
            if full_path not in annotated_images:
                images.append(full_path)
print(f"found {len(images)} files")
print(images[0])

random.shuffle(images)

class Annotator:

    def __init__(self, image) -> None:
        self.start_pos = None
        self.image = image
        self.annotations = []
        self.current_label = 'ball'
        self.image_width = self.image.shape[1]
        self.image_height = self.image.shape[0]
        print(f"Image is {self.image_width}x{self.image_height} px")

    def on_mouse(self, event, x, y, flags, params):
        # print(event, x, y, flags, params)
        if event == 1:
            self.start_pos = (x, y)
        elif event == 4:
            print(self.start_pos, (x, y))
            cv2.rectangle(self.image, self.start_pos, (x, y), class_colors[self.current_label], -1)
            self.annotations.append((self.current_label, self.start_pos, (x, y)))
            self.start_pos = None
        elif event == 3:
            pass

    def has_annotations(self):
        return len(self.annotations) > 0

    def print_annotations(self, file=sys.stdout, scale_factor=1.0):
        for label, start, end in self.annotations:
            center_x = ((start[0] + end[0]) / 2) / self.image_width
            center_y = ((start[1] + end[1]) / 2) / self.image_height
            width =  (np.max([start[0], end[0]]) - np.min([start[0], end[0]])) / self.image_width
            height = (np.max([start[1], end[1]]) - np.min([start[1], end[1]])) / self.image_height
            print(f"{class_ids[label]} {center_x} {center_y} {width} {height}", file=file)

label = 'ball'

output_dir = 'datasets'
train_dir = os.path.join(output_dir, 'train')
val_dir = os.path.join(output_dir, 'val')

train_image_dir = os.path.join(train_dir, 'images')
train_label_dir = os.path.join(train_dir, 'labels')

os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)

val_image_dir = os.path.join(val_dir, 'images')
val_label_dir = os.path.join(val_dir, 'labels')

os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

def add_image_to_dataset(path: str, annotator: Annotator, scale_factor, val_probability=0.2) -> None:
    dest_image_dir = train_image_dir
    dest_label_dir = train_label_dir
    if random.uniform(0, 1) < val_probability:
        dest_image_dir = val_image_dir
        dest_label_dir = val_label_dir

    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        data = f.read()
        md5.update(data)
        image_path = os.path.join(dest_image_dir, f"{md5.hexdigest()}.{path.split('.')[-1]}")
        label_path = os.path.join(dest_label_dir, f"{md5.hexdigest()}.txt")
    
    with open(image_path, "wb") as f:
        f.write(data)

    with open(label_path, "w") as f:
        annotator.print_annotations(f, scale_factor)
try:
    for path in images:
        image = cv2.imread(path)
        print(path)
        scale_factor = 1080 / np.max(image.shape)
        scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
        annotator = Annotator(scaled_image)
        annotator.current_label = label
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", annotator.on_mouse)
        while True:
            cv2.imshow("Image", scaled_image)
            key = cv2.waitKey(20)
            if key == ord('q'):
                if annotator.has_annotations():
                    annotator.print_annotations(scale_factor=1.0/scale_factor)
                    add_image_to_dataset(path, annotator, 1.0 / scale_factor, 0.2)
                    annotated_images.add(path)
                break

except KeyboardInterrupt:
    with open("annotated_images.txt", "w") as f:
        for img in annotated_images:
            print(img, file=f)