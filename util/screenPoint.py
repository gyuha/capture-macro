from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class ScreenPoint(QWidget):
    selectPoint = pyqtSignal(int, int)
    win = ""

    @classmethod
    def run(cls, monitor=0):
        cls.win = cls()
        cls.win.setRect(monitor)
        cls.win.show()
        return cls.win

    def __init__(self, parent=None):
        super(ScreenPoint, self).__init__(parent)

    def setRect(self, monitor):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("""background-color:black; """)
        self.setWindowOpacity(0.3)
        desktopRect = QDesktopWidget().screenGeometry(monitor)
        self.setGeometry(desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.startPoint = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.selectPoint.emit(event.pos().x(), event.pos().y())
            self.close()


if __name__ == "__main__":
    # app = QApplication.instance() or QApplication(sys.argv)
    # WScreenShot.run()
    # app.exec_()

    app = QApplication(sys.argv)
    win = ScreenPoint()
    win.show()
    app.exec_()

    # app = QApplication(sys.argv)
    # win = DesktopChosenBox(700, 500, 30)
    # win.show()
    # app.exec_()
