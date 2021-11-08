import os
import sys
import time

import pyautogui
import pyautogui as pag
import pygetwindow as gw
import pydirectinput
import mozjpeg_lossless_optimization

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from core import mainCore


class ActionController(QObject):
    actionDone = pyqtSignal()
    addImage = pyqtSignal(str)

    def activeWindow(self, title):
        try:
            # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
            win = gw.getWindowsWithTitle(title)[-1]
            if win.isActive == False:
                pywinauto.application.Application().connect(
                    handle=win._hWnd).top_window().set_focus()
            win.activate()  # 윈도우 활성화
        except Exception:
            print(Exception)

    def __init__(self):
        super().__init__()
        self.running = False
        self.core = mainCore()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def setAction(self, action, value):
        if action == "delay":
            timeout = int(value)
        else:
            timeout = 100
        try:
            QTimer.singleShot(timeout, lambda: self.runAction(action, value))
        except Exception as e:
            print(e)

    def captureImage(self, value):
        point = value.split(',')
        if len(point) < 4:
            raise Exception('Invalid capture point')
        screenshot = QApplication.primaryScreen().grabWindow(
            QApplication.desktop().winId())
        rect = QRect(QPoint(int(point[0]), int(point[1])),
                     QPoint(int(point[2]), int(point[3])))
        outputRegion = screenshot.copy(rect)
        path = os.path.join(self.core.newFilePath())
        print('📢[actionController.py:67]:', path)
        outputRegion.save(path, format='JPG', quality=80)

        # JPG 추가 압축히기
        # https: // github.com/wanadev/mozjpeg-lossless-optimization
        with open(path, "rb") as input_jpeg_file:
            input_jpeg_bytes = input_jpeg_file.read()

        output_jpeg_bytes = mozjpeg_lossless_optimization.optimize(
            input_jpeg_bytes)

        with open(path, "wb") as output_jpeg_file:
            output_jpeg_file.write(output_jpeg_bytes)

        self.addImage.emit(path)

    def runAction(self, action, value):
        if self.running == False:
            return

        if action == "capture":
            try:
                self.captureImage(value)
                # time.sleep(0.3)
            except Exception as e:
                print(e)
        elif action == "click":
            try:
                point = value.split(',')
                if len(point) < 2:
                    raise Exception('Invalid click point')
                    return
                # pyautogui.moveTo(int(point[0], int(point[1])))
                # pyautogui.click()
                pyautogui.moveTo(int(point[0]), int(point[1]), 0.05)
                pydirectinput.click()
                # pyautogui.moveTo(int(point[0]), int(point[1]), 0.2)
                # time.sleep(0.2)
                # pyautogui.click()
            except Exception as e:
                print(e)
        elif action == "scroll":
            point = value.split(',')
            if len(point) == 2:
                pyautogui.moveTo(x=int(point[0]), y=int(point[1]))
            pyautogui.scroll(-20)
        elif action == "key":
            pyautogui.press(value)
        elif action == "swipeLeft":
            point = value.split(',')
            x = int(point[0])
            y = int(point[1])
            pydirectinput.moveTo(x=x, y=y, duration=0.1)
            pydirectinput.mouseDown()
            for i in range(4):
                pydirectinput.move(-300, None)
            pydirectinput.mouseUp()
        elif action == "swipeRight":
            point = value.split(',')
            pyautogui.dragTo(x=int(point[0]), y=int(point[1]), duration=0.1)
            pyautogui.dragRel(
                x=(int(point[0]) + 50), y=int(point[1]), duration=0.2)

        self.actionDone.emit()

    def stopAction(self):
        self.running = False
