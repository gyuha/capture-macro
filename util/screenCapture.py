import ctypes
import os

import mozjpeg_lossless_optimization
import mss
import mss.tools
import pyautogui
import win32gui
from PIL import Image, ImageGrab
from PyQt5.QtWidgets import QApplication
from screeninfo import get_monitors

from core import mainCore
from util.screensRatio import ScreensRatio


class ScreenCapture:
    def __init__(self) -> None:
        self.core = mainCore()
        self.screensRatio = ScreensRatio()
        # self.get_monitors_scaling()

    def optimization(self, path):
        """_summary_
        JPG 추가 압축히기
         - https: // github.com/wanadev/mozjpeg-lossless-optimization
        """
        with open(path, "rb") as input_jpeg_file:
            input_jpeg_bytes = input_jpeg_file.read()

        output_jpeg_bytes = mozjpeg_lossless_optimization.optimize(input_jpeg_bytes)

        with open(path, "wb") as output_jpeg_file:
            output_jpeg_file.write(output_jpeg_bytes)

    def shut(self, value, monitor_number=0) -> str:
        point = [int(x) for x in value.split(",")]
        if len(point) < 3:
            raise Exception("Invalid capture point")

        x, y, width, height = (
            point[1],
            point[0],
            point[2] - point[0],
            point[3] - point[1],
        )

        monitors = get_monitors()

        if monitor_number > len(monitors) or monitor_number < 1:
            print(f"Monitor {monitor_number} not found.")
            return

        path = os.path.join(self.core.newFilePath())

        with mss.mss() as sct:
            monitor = sct.monitors[monitor_number]
            capture_area = {
                "left": monitor["left"] + x,
                "top": monitor["top"] + y,
                "width": width,
                "height": height,
                "mon": monitor_number,
            }
            sct_img = sct.grab(capture_area)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

            img.save(path, "JPEG", quality=self.core.config["imageQuality"])

            self.optimization(path)

        return path
