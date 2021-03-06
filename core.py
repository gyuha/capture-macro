import os
from libs.qtSingleton import QtSingleton
import json

macroActions = ["capture", "delay", "click",
                "key", "scroll"]

defaultOptions = {
    "capturePath": "./capture",
    "windowName": "eBook",
    "monitor": 0,
    "sameCount": 3,
    "imageQuality": 80,
    "macro": [
        {'action': 'capture', 'value': '120,122,1610,2041'},
        {'action': 'click', 'value': '1620,1097'},
        {'action': 'delay', 'value': '1000'}
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
        self.imageQuality = 80

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
