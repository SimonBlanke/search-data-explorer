import os
import time
import socket
import subprocess
import cv2

from seleniumbase import BaseCase


from search_data_explorer import SearchDataExplorer


here = os.path.dirname(os.path.realpath(__file__))


def next_free_port(port=8501, max_port=65535):
    # from: https://codereview.stackexchange.com/questions/216037/python-scanner-for-the-first-free-port-in-a-range
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while port <= max_port:
        try:
            sock.bind(("", port))
            sock.close()
            return port
        except OSError:
            port += 1
    raise IOError("no free ports")


class GuiTests(BaseCase):
    def test_stuff_0(self):
        port = str(next_free_port())
        path = os.path.join(here, "run_sde.py")

        print("Selected port:", port)
        print("path", path)

        subprocess.Popen(["python", path, port])
        time.sleep(5)

        self.open("https://localhost:" + str(port))
        time.sleep(1)

        current_screenshot_path = os.path.join(here, "current-screenshot.png")
        self.save_screenshot(current_screenshot_path)

        # test screenshots look exactly the same
        original = cv2.imread(os.path.join(here, "test_images/screenshot.png"))
        duplicate = cv2.imread(current_screenshot_path)

        assert original.shape == duplicate.shape

        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)
        assert cv2.countNonZero(b) == cv2.countNonZero(g) == cv2.countNonZero(r) == 0

        os.remove(current_screenshot_path)
