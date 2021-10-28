import os
def event(OCR, pos_1, pos_2):
    OCR.catchScreenOfWindow((pos_1[0],pos_1[1]),(pos_2[0],pos_2[1]))
    OCR.catchStringFromImage()
    # OCR.getRidOfScreen()
    return OCR.imageString