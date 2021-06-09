import os
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from core import mainCore

import pyautogui as pag
import pywinauto
import pygetwindow as gw


class ActionController(QObject):
    actionDone = pyqtSignal()
    addImage = pyqtSignal(str)

    def activeWindow(self, title):
        try:
            # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
            win = gw.getWindowsWithTitle(title)[0]
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

    def runAction(self, action, value):
        if self.running == False:
            return

        if action == "capture":
            try:
                # scrcpy = ScrCpyCapture()
                # path = os.path.join(self.core.newFilePath())
                # scrcpy.capture(path)
                # get_screen('./capture/a.png')
                time.sleep(0.3)
                # self.addImage.emit(path)
            except Exception as e:
                print(e)
        elif action == "click":
            print(value)
            try:
                size = value.split(',')
                if len(size) < 4:
                    print(size)
                    return
            except Exception as e:
                print(e)
        elif action == "key":
            print(action)
            # send_adb_key(value)

        print(action)
        print(value)

        self.actionDone.emit()

    def sendKey(self, key):
        send_adb_key(key)

    def stopAction(self):
        self.running = False
