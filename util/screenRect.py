# from Qt import __binding__
#
# print(__binding__)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

'''
Cannot import QScreen class in # Qt
try:
    from PySide2.QtGui import QScreen
except:
    from PyQt5.QtGui import QScreen
'''
import sys


class ScreenRect(QWidget):
    selectedRect = pyqtSignal(int, int, int, int)
    win = ''
    #

    @classmethod
    def run(cls):
        cls.win = cls()
        cls.win.show()

    def __init__(self, parent=None):
        super(ScreenRect, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        # desktop = QApplication.desktop()
        # rect = desktop.availableGeometry()
        desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.isDrawing = False
        self.startPoint = QPoint()
        self.endPoint = QPoint()

    def paintEvent(self, event):
        if self.isDrawing:
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen)
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.startPoint, self.endPoint))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True

    def mouseMoveEvent(self, event):
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()

            x1 = self.startPoint.x() if self.startPoint.x(
            ) < self.endPoint.x() else self.endPoint.x()
            x2 = self.startPoint.x() if self.startPoint.x(
            ) > self.endPoint.x() else self.endPoint.x()
            y1 = self.startPoint.y() if self.startPoint.y(
            ) < self.endPoint.y() else self.endPoint.y()
            y2 = self.startPoint.y() if self.startPoint.y(
            ) > self.endPoint.y() else self.endPoint.y()

            self.startPoint = QPoint()
            self.endPoint = QPoint()
            self.update()

            self.selectedRect.emit(x1, y1, x2, y2)
            # PySide2
            # screenshot = QPixmap.grabWindow(QApplication.desktop().winId())
            # PyQt5
            # screenshot = QApplication.primaryScreen().grabWindow(0)

            # screenshot = QApplication.primaryScreen().grabWindow(
            #     QApplication.desktop().winId())
            # rect = QRect(startPoint, endPoint)
            # outputRegion = screenshot.copy(rect)
            # outputRegion.save('d:/sho54t.jpg', format='JPG', quality=100)
            self.close()


if __name__ == '__main__':
    # app = QApplication.instance() or QApplication(sys.argv)
    # WScreenShot.run()
    # app.exec_()

    app = QApplication(sys.argv)
    win = ScreenRect()
    win.show()
    app.exec_()

    # app = QApplication(sys.argv)
    # win = DesktopChosenBox(700, 500, 30)
    # win.show()
    # app.exec_()
