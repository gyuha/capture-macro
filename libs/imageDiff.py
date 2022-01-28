import re
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import numpy as np

class ImageDiff():
    def __init__(self):
        self.preImage = None

    def reset(self):
        self.preImage = None
    
    def readFile(self, filePath):
        image = cv2.imread(filePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def diff(self, imagePath):
        print('📢[imageDiff.py:18]: ', imagePath)
        if (self.preImage is None):
            self.preImage = self.readFile(imagePath)
            return False
        currentImage = self.readFile(imagePath)

        (score, diff) = compare_ssim(self.preImage, currentImage, full=True)
        diff = (diff * 255).astype("uint8")
        print('📢[imageDiff.py:17]: ', score)
        self.preImage = currentImage
        return False if score > 1.0 else True