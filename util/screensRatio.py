from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication, QScreen


class ScreensRatio:
    def __init__(self) -> None:
        # 각 스크린의 정보를 가져옵니다.
        screens = QGuiApplication.screens()

        # 각 스크린에 대한 처리를 수행합니다.
        for i, screen in enumerate(screens):
            logical_dpi = screen.logicalDotsPerInch()
            physical_dpi = screen.physicalDotsPerInch()
            geometry = screen.geometry()

            # 모니터의 크기를 계산합니다.
            monitor_width = geometry.width()
            monitor_height = geometry.height()
            monitor_width_inch = monitor_width / logical_dpi
            monitor_height_inch = monitor_height / logical_dpi

            # 현재 화면 비율을 계산합니다.
            current_ratio = physical_dpi / logical_dpi

            # 확대 비율을 설정합니다.
            zoom_ratio = 2  # 200% 확대

            # 확대된 모니터의 크기를 계산합니다.
            zoomed_monitor_width_inch = monitor_width_inch / zoom_ratio
            zoomed_monitor_height_inch = monitor_height_inch / zoom_ratio
            zoomed_monitor_width_pixel = (
                zoomed_monitor_width_inch * logical_dpi * current_ratio
            )
            zoomed_monitor_height_pixel = (
                zoomed_monitor_height_inch * logical_dpi * current_ratio
            )

            # 결과를 출력합니다.
            print(
                f"모니터 {i+1} 크기: {monitor_width} x {monitor_height} 픽셀, {monitor_width_inch:.2f} x {monitor_height_inch:.2f} 인치"
            )
            print(f"모니터 {i+1} 현재 화면 비율: {current_ratio:.2f}")
            print(
                f"모니터 {i+1} 확대된 모니터 크기: {zoomed_monitor_width_pixel:.0f} x {zoomed_monitor_height_pixel:.0f} 픽셀"
            )
