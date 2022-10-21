import cv2
import pytesseract

class Recognition:
    def __init__(self, image) -> None:
        self.image = image
        self.setConfig(r'--oem 3 --psm 6 -l rus')

    def setConfig(self, config):
        self.config = config

    def doRecognition(self) -> str:
        return pytesseract.image_to_string(self.image, config = self.config)
        