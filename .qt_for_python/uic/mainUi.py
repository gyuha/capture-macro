# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\workspace\capture-macro\mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1520, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.edtCapturePath = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.edtCapturePath.setFont(font)
        self.edtCapturePath.setAccessibleName("")
        self.edtCapturePath.setObjectName("edtCapturePath")
        self.gridLayout.addWidget(self.edtCapturePath, 0, 0, 1, 1)
        self.btnPathSelect = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnPathSelect.setFont(font)
        self.btnPathSelect.setAccessibleName("")
        self.btnPathSelect.setObjectName("btnPathSelect")
        self.gridLayout.addWidget(self.btnPathSelect, 0, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.leActiveWindowName = QtWidgets.QLineEdit(self.centralwidget)
        self.leActiveWindowName.setObjectName("leActiveWindowName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leActiveWindowName)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.macroTable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.macroTable.setFont(font)
        self.macroTable.setRowCount(0)
        self.macroTable.setObjectName("macroTable")
        self.macroTable.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.macroTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.macroTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.macroTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.macroTable.setHorizontalHeaderItem(3, item)
        self.macroTable.verticalHeader().setVisible(True)
        self.macroTable.verticalHeader().setHighlightSections(True)
        self.verticalLayout_4.addWidget(self.macroTable)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lbConfigFilePath = QtWidgets.QLabel(self.centralwidget)
        self.lbConfigFilePath.setObjectName("lbConfigFilePath")
        self.horizontalLayout_5.addWidget(self.lbConfigFilePath)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.leCurrentCount = QtWidgets.QLineEdit(self.centralwidget)
        self.leCurrentCount.setEnabled(False)
        self.leCurrentCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leCurrentCount.setObjectName("leCurrentCount")
        self.horizontalLayout_6.addWidget(self.leCurrentCount)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.leTotalCount = QtWidgets.QLineEdit(self.centralwidget)
        self.leTotalCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leTotalCount.setObjectName("leTotalCount")
        self.horizontalLayout_6.addWidget(self.leTotalCount)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnConfigInsert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfigInsert.setObjectName("btnConfigInsert")
        self.horizontalLayout_4.addWidget(self.btnConfigInsert)
        self.btnConfigAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfigAdd.setObjectName("btnConfigAdd")
        self.horizontalLayout_4.addWidget(self.btnConfigAdd)
        self.btnConfigRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfigRemove.setObjectName("btnConfigRemove")
        self.horizontalLayout_4.addWidget(self.btnConfigRemove)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnCapture.setFont(font)
        self.btnCapture.setObjectName("btnCapture")
        self.horizontalLayout.addWidget(self.btnCapture)
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbFileList = QtWidgets.QLabel(self.centralwidget)
        self.lbFileList.setObjectName("lbFileList")
        self.verticalLayout_3.addWidget(self.lbFileList)
        self.lsFiles = QtWidgets.QListWidget(self.centralwidget)
        self.lsFiles.setFrameShape(QtWidgets.QFrame.Box)
        self.lsFiles.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lsFiles.setIconSize(QtCore.QSize(80, 120))
        self.lsFiles.setTextElideMode(QtCore.Qt.ElideLeft)
        self.lsFiles.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.lsFiles.setGridSize(QtCore.QSize(0, 120))
        self.lsFiles.setViewMode(QtWidgets.QListView.ListMode)
        self.lsFiles.setObjectName("lsFiles")
        self.verticalLayout_3.addWidget(self.lsFiles)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnToPdf = QtWidgets.QPushButton(self.centralwidget)
        self.btnToPdf.setObjectName("btnToPdf")
        self.horizontalLayout_3.addWidget(self.btnToPdf)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnDeleteFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteFile.setObjectName("btnDeleteFile")
        self.horizontalLayout_3.addWidget(self.btnDeleteFile)
        self.btnDeleteAllFiles = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteAllFiles.setObjectName("btnDeleteAllFiles")
        self.horizontalLayout_3.addWidget(self.btnDeleteAllFiles)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.lbPreview = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbPreview.setFont(font)
        self.lbPreview.setAutoFillBackground(True)
        self.lbPreview.setText("")
        self.lbPreview.setObjectName("lbPreview")
        self.horizontalLayout_2.addWidget(self.lbPreview)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1520, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSaveAs)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caputre automate"))
        self.label_4.setText(_translate("MainWindow", "Capture automate"))
        self.label.setText(_translate("MainWindow", "저장경로"))
        self.edtCapturePath.setText(_translate("MainWindow", "./caputre"))
        self.btnPathSelect.setText(_translate("MainWindow", "선택"))
        self.label_8.setText(_translate("MainWindow", "윈도우 이름"))
        self.label_2.setText(_translate("MainWindow", "실행"))
        item = self.macroTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "명령어"))
        item = self.macroTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "값"))
        item = self.macroTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "동작"))
        item = self.macroTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "동작2"))
        self.label_6.setText(_translate("MainWindow", "파일명 :"))
        self.lbConfigFilePath.setText(_translate("MainWindow", "./default.json"))
        self.label_5.setText(_translate("MainWindow", "현재 : "))
        self.leCurrentCount.setInputMask(_translate("MainWindow", "9999"))
        self.leCurrentCount.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "/ 전체 :"))
        self.leTotalCount.setInputMask(_translate("MainWindow", "9999"))
        self.leTotalCount.setText(_translate("MainWindow", "1000"))
        self.btnConfigInsert.setText(_translate("MainWindow", "명령어 삽입"))
        self.btnConfigAdd.setText(_translate("MainWindow", "명령어 추가"))
        self.btnConfigRemove.setText(_translate("MainWindow", "명령어 삭제"))
        self.btnCapture.setText(_translate("MainWindow", " 캡쳐"))
        self.btnStart.setText(_translate("MainWindow", "시작"))
        self.btnStop.setText(_translate("MainWindow", "정지 (F2)"))
        self.lbFileList.setText(_translate("MainWindow", "파일 목록"))
        self.btnToPdf.setText(_translate("MainWindow", "PDF로 저장"))
        self.btnDeleteFile.setText(_translate("MainWindow", "삭제"))
        self.btnDeleteAllFiles.setText(_translate("MainWindow", "전체 삭제"))
        self.menu.setTitle(_translate("MainWindow", "파일"))
        self.actionOpen.setText(_translate("MainWindow", "열기(&o)"))
        self.actionSave.setText(_translate("MainWindow", "저장(&s)"))
        self.actionSaveAs.setText(_translate("MainWindow", "다른 이름으로 저장"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
