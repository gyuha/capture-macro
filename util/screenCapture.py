import os
import mozjpeg_lossless_optimization
import pyautogui

from core import mainCore

from screeninfo import get_monitors

from PIL import Image


class ScreenCapture:
    def __init__(self) -> None:
        self.core = mainCore()

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

        # 선택한 모니터의 위치 및 크기 가져오기
        monitor = monitors[monitor_number - 1]
        monitor_x, monitor_y, monitor_width, monitor_height = (
            monitor.x,
            monitor.y,
            monitor.width,
            monitor.height,
        )

        # 지정한 좌표와 크기로 캡쳐
        screenshot = pyautogui.screenshot(
            region=(monitor_x + x, monitor_y + y, width, height)
        )
        path = os.path.join(self.core.newFilePath())
        screenshot.save(path, format="JPEG", quality=self.core.config["imageQuality"])

        self.optimization(path)

        return path
