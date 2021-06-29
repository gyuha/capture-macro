import glob
import io
import os
import re
import sys
import time
from pathlib import Path

import keyboard

import pyperclip
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, uic
from PyQt5.QtCore import QDir, Qt, pyqtSlot
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import *

import mainUi
from actionController import ActionController
from core import macroActions, mainCore
from imageToPdfWorker import ImageToPdfWorker
from libs.fileUtil import removePathFiles
from util.screenPoint import ScreenPoint
from util.screenRect import ScreenRect
from functools import partial

# form_class = uic.loadUiType("mainUi.ui")[0]


class MainWindow(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.core = mainCore()

        self.setWindowIcon(QIcon('icon.ico'))

        self.setConfigSet()

        self.actionOpen.triggered.connect(self.clickConfigLoad)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionSave.triggered.connect(self.clickConfigSave)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSaveAs.triggered.connect(self.clickConfigSaveAs)
        self.actionSaveAs.setShortcut('Ctrl+Shift+S')

        self.lbConfigFilePath.setText(self.core.configPath)
        self.btnConfigInsert.clicked.connect(self.clickConfigInsert)
        self.btnConfigAdd.clicked.connect(self.clickConfigAdd)
        self.btnConfigRemove.clicked.connect(self.clickConfigRemove)
        self.btnPathSelect.clicked.connect(self.clickSelectPath)

        self.btnCapture.clicked.connect(self.clickCapture)
        self.btnStart.clicked.connect(self.clickStart)
        self.btnStop.clicked.connect(self.clickStop)

        self.btnToPdf.clicked.connect(self.clickToPdf)

        self.btnDeleteFile.clicked.connect(self.clickDeleteSelectFile)
        self.btnDeleteAllFiles.clicked.connect(self.clickDeleteAllFiles)

        self.lsFiles.itemSelectionChanged.connect(self.onCaptureFileChanged)

        self.selectRow = 0

        self.actionController = ActionController()
        self.actionController.actionDone.connect(self.actionDone)
        self.actionController.addImage.connect(self.addImage)

        self.loadCaptureFiles()
        self.setButtonState(False)

        self.savePdfWorker = ImageToPdfWorker()
        self.savePdfWorker.updateProgress.connect(self.updateProgress)

        self.btnPointClick.clicked.connect(self.clickPointClick)
        self.screenPoint = ScreenPoint()
        self.screenPoint.selectPoint.connect(self.onSelectPoint)

        self.btnScreenRect.clicked.connect(self.clickScreenRect)
        self.screenRect = ScreenRect()
        self.screenRect.selectedRect.connect(self.onSelectRect)

        keyboard.add_hotkey('f1', self.clickStart)
        keyboard.add_hotkey('f2', self.clickStop)

    def setButtonState(self, enabled):
        bWorking = enabled
        self.btnPathSelect.setEnabled(not bWorking)
        self.btnConfigInsert.setEnabled(not bWorking)
        self.btnConfigAdd.setEnabled(not bWorking)
        self.btnConfigRemove.setEnabled(not bWorking)
        self.btnCapture.setEnabled(not bWorking)
        self.btnStart.setEnabled(not bWorking)

        self.btnStop.setEnabled(bWorking)

    def setLsFiles(self, path):
        self.model = QFileSystemModel()
        # self.model.setRootPath(path)
        # self.index_root = self.model.index(self.model.rootPath())
        # self.lsFiles.setRootIndex(self.index_root)

    @pyqtSlot(int)
    def clickTableCaptureArea(self, row):
        print('📢[main.py:105]:', row)
        print('click')

    def getMacroTableRow(self, row, action, value):
        actionCombo = QComboBox()
        actionCombo.currentTextChanged.connect(self.updateMacroActions)
        actionCombo.addItems(macroActions)
        index = actionCombo.findText(action)
        if index > -1:
            actionCombo.setCurrentIndex(index)
        # actionCombo.currentTextChanged.connect(self.onActionComboChange)

        self.macroTable.setCellWidget(
            row, 0, actionCombo)

        item = QTableWidgetItem(value)
        self.macroTable.setItem(row, 1, item)

    def setConfigSet(self):
        self.edtCapturePath.setText(self.core.config['capturePath'])
        self.leActiveWindowName.setText(self.core.config['windowName'])
        self.leScreenRect.setText(self.core.config['screenRect'])
        self.leClickPoint.setText(self.core.config['clickPoint'])
        self.macroTable.setRowCount(0)
        self.macroTable.setRowCount(len(self.core.config['macro']))
        self.macroTable.setAlternatingRowColors(True)
        self.macroTable.setColumnWidth(0, 100)
        self.macroTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        for row, macro in enumerate(self.core.config['macro']):
            self.getMacroTableRow(row, macro['action'], macro['value'])
        self.updateMacroActions()

    @pyqtSlot(str)
    def onActionComboChange(self, txt):
        # print(txt)
        combo = self.sender()
        row = combo.currentRow()
        self.core.config['macro'][row]['action'] = txt

    def clickConfigLoad(self):
        path = QFileDialog.getOpenFileName(
            self, "Select Config file", "", "JSON (*.json)")
        if path[0]:
            self.core.configPath = path[0]
            self.lbConfigFilePath.setText(self.core.configPath)
            self.core.loadMacro()
            self.setConfigSet()

    def clickConfigSave(self):
        self.core.config['macro'] = []
        self.core.config['windowName'] = self.leActiveWindowName.text()
        self.core.config['screenRect'] = self.leScreenRect.text()
        self.core.config['clickPoint'] = self.leClickPoint.text()
        for row in range(self.macroTable.rowCount()):
            action = self.macroTable.cellWidget(row, 0).currentText()
            value = self.macroTable.item(row, 1).text()
            self.core.config['macro'].append(
                {"action": action, "value": value})
        self.core.saveMacro()
        QMessageBox.information(self, "Information", "저장 완료")

    def updateMacroActions(self):
        try:
            for row in range(self.macroTable.rowCount()):
                action = self.macroTable.cellWidget(row, 0).currentText()
                self.macroTable.removeCellWidget(row, 2)
                self.macroTable.removeCellWidget(row, 3)
                if action == 'capture':
                    button = QPushButton()
                    button.setText('영역선택')
                    button.clicked.connect(
                        partial(self.clickTableCaptureArea, row))
                    button2 = QPushButton()
                    button2.setText('확인')
                    button2.clicked.connect(
                        partial(self.clickTableCaptureArea, row))
                    self.macroTable.setCellWidget(row, 2, button)
                    self.macroTable.setCellWidget(row, 3, button2)
                elif action == 'click' or action == 'scroll':
                    button = QPushButton()
                    button.setText('포인트')
                    button.clicked.connect(
                        partial(self.clickTableCaptureArea, row))
                    self.macroTable.setCellWidget(row, 2, button)
                else:
                    item = QTableWidgetItem()
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    self.macroTable.setItem(row, 2, item)
                    self.macroTable.setItem(row, 3, item)
        except Exception as e:
            pass

    def clickConfigSaveAs(self):
        path = QFileDialog.getSaveFileName(
            self, 'Save File', "", "JSON (*.json)")

        self.core.config['capturePath'] = self.edtCapturePath.text()
        self.core.config['windowName'] = self.leActiveWindowName.text()
        self.core.config['screenRect'] = self.leScreenRect.text()
        self.core.config['clickPoint'] = self.leClickPoint.text()

        self.core.configPath = path[0]
        self.core.config['macro'] = []

        for row in range(self.macroTable.rowCount()):
            action = self.macroTable.cellWidget(row, 0).currentText()
            value = self.macroTable.item(row, 1).text()
            self.core.config['macro'].append(
                {"action": action, "value": value})
        self.core.saveMacro()

        self.lbConfigFilePath.setText(self.core.configPath)
        self.core.loadMacro()
        self.setConfigSet()
        QMessageBox.information(self, "Information", "저장 완료")

    def clickConfigInsert(self):
        row = self.macroTable.currentRow()
        self.macroTable.insertRow(row)
        self.getMacroTableRow(row, 'capture', '')
        self.updateMacroActions()

    def clickConfigAdd(self):
        row = self.macroTable.currentRow()
        self.macroTable.insertRow(row+1)
        self.getMacroTableRow(row+1, 'capture', '')
        self.updateMacroActions()

    def clickConfigRemove(self):
        row = self.macroTable.currentRow()
        self.macroTable.removeRow(row)

    def onMacroTableChanged(self):
        text = self.macroTable.currentItem().text()

    def setCapturePath(self, path):
        path = str(QFileDialog.getExistingDirectory(self, "경로 선택"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path
        self.loadCaptureFiles()

    def clickSelectPath(self):
        print("select path Clicked")
        path = str(QFileDialog.getExistingDirectory(self, "경로 선택"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path
        self.loadCaptureFiles()

    def clickStop(self):
        self.setButtonState(False)
        print("stop Clicked", self.core.capturePath)
        self.actionController.stop()
        self.actionController.stopAction()
        self.macroTable.setDisabled(False)

    def checkStop(self):
        flag = int(self.leTotalCount.text()) < self.core.fileNumber
        if flag:
            self.clickStop()
        return flag

    def clickStart(self):
        print('📢[main.py:220]:', self.core.config['windowName'])
        self.actionController.activeWindow(self.leActiveWindowName.text())

        if (self.checkStop()):
            return
        self.setButtonState(True)
        print("start Clicked")
        self.macroTable.setDisabled(True)
        self.selectRow = 0
        self.macroTable.selectRow(self.selectRow)

        self.actionController.start()
        self.selectRow = 0
        self.macroTable.selectRow(self.selectRow)
        action, value = self.getRowValues()
        self.actionController.setAction(action, value)

    def getRowValues(self):
        row = self.selectRow
        action = self.macroTable.cellWidget(row, 0).currentText()
        value = self.macroTable.item(row, 1).text()
        return (action, value)

    def nextAction(self):
        if (self.checkStop()):
            return
        self.selectRow = self.selectRow + 1
        if self.selectRow >= self.macroTable.rowCount():
            self.selectRow = 0
        self.macroTable.selectRow(self.selectRow)
        action, value = self.getRowValues()
        self.actionController.setAction(action, value)

    @pyqtSlot()
    def actionDone(self):
        if (self.checkStop()):
            return
        self.nextAction()
        self.leCurrentCount.setText(str(self.core.fileNumber))

    @ pyqtSlot(str)
    def addImage(self, path):
        self.addCaptureFile(path)
        self.lastLsFileSelect()

    def clickCapture(self):
        file = self.core.newFilePath()
        # get_screen(file)
        self.addCaptureFile(file)
        self.lastLsFileSelect()

    def pil2pixmap(self, image):
        bytesImg = io.BytesIO()
        image.save(bytesImg, format='JPEG')

        qImg = QImage()
        qImg.loadFromData(bytesImg.getvalue())

        return QPixmap.fromImage(qImg)

    def loadCaptureFiles(self):
        self.lsFiles.clear()
        Path(self.core.capturePath).mkdir(parents=True, exist_ok=True)
        files = os.listdir(self.core.capturePath)
        for file in files:
            path = os.path.join(self.core.capturePath, file)
            self.addCaptureFile(path)
        self.startFileNumber()

    def startFileNumber(self):
        files = os.listdir(self.core.capturePath)
        p = re.compile('^\d+.jpg$')
        files = [s for s in files if p.match(s)]
        if len(files) == 0:
            self.core.fileNumber = 0
            return
        basename = os.path.basename(files[-1])
        num = int(os.path.splitext(basename)[0])
        self.core.fileNumber = num
        self.leCurrentCount.setText(str(num))

    def addCaptureFile(self, path):
        try:
            # or not (path.endswith(".jpg") and path.endswith(".png")):
            if os.path.isdir(path) or not (path.endswith(".jpg")):
                return
            picture = Image.open(path)
            picture.thumbnail((80, 120), Image.ANTIALIAS)

            icon = QIcon(self.pil2pixmap(picture))
            item = QListWidgetItem(os.path.basename(path), self.lsFiles)
            item.setStatusTip(path)
            item.setIcon(icon)
        except Exception as e:
            print(e)

    def onCaptureFileChanged(self):
        item = self.lsFiles.selectedItems()
        if len(item) > 0:
            path = os.path.join(self.core.capturePath, item[0].text())
            self.previewDisplay(path)

    def previewDisplay(self, path):
        pix = QPixmap()
        pix.load(path)
        pix = pix.scaledToWidth(self.lbPreview.width(),
                                Qt.SmoothTransformation)
        self.lbPreview.setPixmap(pix)

    @ pyqtSlot(int, str)
    def updateProgress(self, count, label):
        if not self.progressDialog.wasCanceled():
            self.progressDialog.setLabelText(label)
            self.progressDialog.setValue(count)
        else:
            QMessageBox.warning(self, "Save file", "abort...")

    def clickToPdf(self):
        fileName = QFileDialog.getSaveFileName(
            self, 'Save file', '', '.pdf')
        if not fileName:
            return
        filePath = fileName[0]
        if not filePath:
            return
        if not fileName[0].endswith(".pdf"):
            filePath = filePath + ".pdf"

        self.progressDialog = QProgressDialog(
            "Save to pdf", "Cancel", 0, 100, self)
        self.progressDialog.setWindowTitle('Save to pdf')

        self.savePdfWorker.setFiles(self.core.capturePath, filePath)
        self.savePdfWorker.start()

        self.progressDialog.setWindowModality(Qt.WindowModal)
        self.progressDialog.forceShow()

        # if fileName[0]:

    def clickDeleteSelectFile(self):
        try:
            item = self.lsFiles.selectedItems()
            row = self.lsFiles.currentRow()
            if len(item) > 0:
                os.remove(os.path.join(self.core.capturePath, item[0].text()))
                self.lsFiles.takeItem(row)
        except Exception as e:
            print(e)

    def clickPointClick(self):
        self.screenPoint.show()

    @pyqtSlot(int, int)
    def onSelectPoint(self, x, y):
        text = f"{x},{y}"
        pyperclip.copy(text)
        self.leClickPoint.setText(text)

    def clickScreenRect(self):
        self.screenRect = self.screenRect.run()
        self.screenRect.selectedRect.connect(self.onSelectRect)

    @pyqtSlot(int, int, int, int)
    def onSelectRect(self, x1, y1, x2, y2):
        text = f"{x1},{y1},{x2},{y2}"
        pyperclip.copy(text)
        self.leScreenRect.setText(text)

    def lastLsFileSelect(self):
        self.lsFiles.setCurrentRow(self.lsFiles.count() - 1)

    def clickDeleteAllFiles(self):
        ret = QMessageBox.question(
            self, "경고", "정말 모든 파일을 지우시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ret == QMessageBox.Yes:
            try:
                for file in ['*.png', '*.jpg']:
                    path = os.path.join(self.core.capturePath, file)
                    files = glob.glob(path)
                    removePathFiles(files)
                self.lsFiles.clear()
                self.startFileNumber()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
