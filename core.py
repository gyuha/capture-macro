import os
from libs.qtSingleton import QtSingleton
import json

macroActions = ["capture", "delay", "click", "key", "scroll"]

defaultOptions = {
    "capturePath": "./capture",
    "windowName": "eBook",
    "clickPoint": "",
    "screenRect": "",
    "macro": [
        {"capture": "", "click": "", "delay": 500}
    ]
}


class mainCore(QtSingleton):
    def __init__(self):
        super().__init__()
        self.capturePath = './capture'
        self.config = defaultOptions
        self.configPath = './default.json'
        self.loadMacro()
        self.fileNumber = 0

    def loadMacro(self):
        """
        json의 데이터를 로딩하기
        """
        try:
            print(self.configPath)
            with open(self.configPath, encoding='utf8') as jsonFile:
                self.config = json.load(jsonFile)
        except Exception as e:
            print(e)
            self.config = defaultOptions

    def saveMacro(self):
        try:
            with open(self.configPath, 'w', encoding='utf8') as jsonFile:
                json.dump(self.config, jsonFile)
        except IOError:
            print(IOError)

    def currentFileName(self):
        return "{:04d}.jpg".format(self.fileNumber)

    def currentFilePath(self):
        return os.path.join(self.config['capturePath'], self.currentFileName())

    def newFilePath(self):
        self.fileNumber = self.fileNumber + 1
        return os.path.join(self.config['capturePath'], self.currentFileName())
