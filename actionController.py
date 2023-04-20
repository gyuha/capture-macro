import time

import mss.tools
import pyautogui
import pydirectinput
import pygetwindow as gw
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core import mainCore
from util.screenCapture import ScreenCapture


class ActionController(QObject):
    actionDone = pyqtSignal()
    addImage = pyqtSignal(str)
    monitor = 0

    def activeWindow(self, title):
        try:
            # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
            win = gw.getWindowsWithTitle(title)[-1]
            if win.isActive is False:
                pywinauto.application.Application().connect(
                    handle=win._hWnd
                ).top_window().set_focus()
            win.activate()  # 윈도우 활성화
        except Exception:
            print(Exception)

    def __init__(self):
        super().__init__()
        self.running = False
        self.core = mainCore()
        self.screenCapture = ScreenCapture()

    def start(self, monitor):
        self.running = True
        self.monitor = monitor

    def stop(self):
        self.running = False

    def setAction(self, action, value, monitor):
        self.monitor = monitor
        if action == "delay":
            timeout = int(value)
        else:
            timeout = 100
        try:
            QTimer.singleShot(timeout, lambda: self.runAction(action, value))
        except Exception as e:
            print(e)

    def captureImage(self, value, monitor=0):
        path = self.screenCapture.shut(value, monitor)
        # 이미지 추가 메시지
        self.addImage.emit(path)

    def runAction(self, action, value):
        if self.running is False:
            return

        if action == "capture":
            try:
                self.captureImage(value, self.monitor)
                # time.sleep(0.3)
            except Exception as e:
                print(e)
        elif action == "click":
            try:
                point = value.split(",")
                if len(point) < 2:
                    raise Exception("Invalid click point")
                    return
                self.mouseMoveTo(value)
                pydirectinput.click()
            except Exception as e:
                print(e)
        elif action == "key":
            try:
                key = value
                pydirectinput.keyDown(key)
                time.sleep(0.3)
                pydirectinput.keyUp(key)
            except Exception as e:
                print(e)
        elif action == "scroll":
            point = value.split(",")
            self.mouseMoveTo(value)
            pyautogui.scroll(-20)
        # elif action == "swipeLeft":
        #     point = value.split(',')
        #     x = int(point[0])
        #     y = int(point[1])
        #     pydirectinput.moveTo(x=x, y=y, duration=0.1)
        #     pydirectinput.mouseDown()
        #     for i in range(4):
        #         pydirectinput.move(-300, None)
        #     pydirectinput.mouseUp()
        # elif action == "swipeRight":
        #     point = value.split(',')
        #     pyautogui.dragTo(x=int(point[0]), y=int(point[1]), duration=0.1)
        #     pyautogui.dragRel(
        #         x=(int(point[0]) + 50), y=int(point[1]), duration=0.2)

        self.actionDone.emit()

    def mouseMoveTo(self, value):
        point = value.split(",")
        if len(point) < 2:
            return
        x = int(point[0])
        y = int(point[1])

        screen_num = self.monitor
        with mss.mss() as sct:
            mon = sct.monitors[screen_num + 1]

        x = x + mon["left"]
        y = y + mon["top"]
        pyautogui.moveTo(x, y, 0.05)

    def stopAction(self):
        self.running = False
