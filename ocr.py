import pyautogui
import pytesseract
from PIL import Image
from pytesseract import image_to_string
from config import tesseract_url
import os
class OCRHandler:
    def __init__(self):
        self.imageString = None
        self.imagePath = os.getcwd() + "\\temp\\"
        self.imageName = "capture.png"
    def catchScreenOfWindow(self,pos_1,pos_2):
        try:
            screen = pyautogui.screenshot(region=(pos_1[0],pos_1[1],pos_2[0],pos_2[1])) 
            screen.save( self.imagePath + self.imageName)
        except:
            print("catch screen exception")
        # screen = pyautogui.screenshot(region=(pos_1[0],pos_1[1],pos_2[0],pos_2[1])) 
        # screen.save( self.imagePath + self.imageName)
    def catchStringFromImage(self):
        try:
            pytesseract.pytesseract.tesseract_cmd = r'{}'.format(tesseract_url)
            self.imageString = image_to_string(Image.open(self.imagePath + self.imageName), lang='eng')
        except:
            print("load string exception")
        # pytesseract.pytesseract.tesseract_cmd = r'{}'.format(tesseract_url)
        # self.imageString = image_to_string(Image.open(self.imagePath + self.imageName), lang='eng')
        # print(self.imageString)
    def getRidOfScreen(self):
        os.chdir(self.path)
        for file in os.listdir(self.path):
            if file.endswith(".png"):
                file_name = os.path.basename(self.path + self.imageName)
                if file_name == self.imageName:
                    os.remove( self.imagePath + file)
        