import socket
import struct
import threading
from queue import SimpleQueue


class RobotJpegImageStream:
    images_upper_cam: SimpleQueue[bytes]
    images_lower_cam: SimpleQueue[bytes]

    max_images_in_queue = 5

    def __init__(self, ipaddr: str, port: int = 9999):
        self.images_upper_cam = SimpleQueue()
        self.images_lower_cam = SimpleQueue()
        threading.Thread(target=self._receive_image_thread, name="RobotJpegReceiver", args=(ipaddr, port),
                         daemon=True).start()

    def _discard_old_images(self, q: SimpleQueue[bytes]):
        while q.qsize() > self.max_images_in_queue:
            q.get()

    def _receive_image_thread(self, ipaddr: str, port: int):
        sock = socket.create_connection((ipaddr, port))
        fp = sock.makefile("rb")

        while True:
            length, is_lower_cam = struct.unpack(">ib", fp.read(5))
            buf = fp.read(length)

            if is_lower_cam != 0:
                self.images_lower_cam.put(buf)
                self._discard_old_images(self.images_lower_cam)
            else:
                self.images_upper_cam.put(buf)
                self._discard_old_images(self.images_upper_cam)
