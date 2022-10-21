import cv2

class ImageProcessor:
    def __init__(self, imageFileName: str) -> None:
        self.img = cv2.imread(imageFileName)

    def togreyscale(self):
        greyscale = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img = greyscale

    def toNegative(self):
        self.img = cv2.bitwise_not(self.img)

    def thresholding(self):
        thr = cv2.threshold(self.img, thresh=0, maxval=127, type=cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
        self.img = thr

    def canny(self):
        cannied = cv2.Canny(self.img, 100, 200)
        self.img = cannied

    # options: 'greyscale', 'thresholding', 'canny', negative
    def preprocImage(self, options = ['greyscale']):
        if 'greyscale' in options: 
            self.togreyscale()
        if 'negative' in options:
            self.toNegative()
        if 'thresholding' in options: 
            self.thresholding()
        if 'canny' in options: 
            self.canny()
        return self.img
