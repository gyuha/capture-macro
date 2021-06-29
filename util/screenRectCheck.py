from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class ScreenRectCheck(QWidget):
    win = ''

    def __init__(self, parent=None):
        super(ScreenRectCheck, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.5)
        desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(desktopRect)
        # self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.setMouseTracking(True)

    @classmethod
    def run(cls, value):
        point = value.split(',')
        if len(point) < 4:
            raise Exception('Invalid capture point')

        cls.win = cls()
        pp = QPainter(cls.win.mask)
        pen = QPen()
        pen.setStyle(Qt.NoPen)
        pp.setPen(pen)
        brush = QBrush(Qt.white)
        pp.setBrush(brush)
        rect = QRect(QPoint(int(point[0]), int(point[1])),
                     QPoint(int(point[2]), int(point[3])))
        pp.drawRect(rect)
        cls.win.setMask(QBitmap(cls.win.mask))

        cls.win.show()
        return cls.win

    def mousePressEvent(self, event):
        self.close()
