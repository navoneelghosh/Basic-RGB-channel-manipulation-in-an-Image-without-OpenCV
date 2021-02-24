# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:45:28 2021

@author: Navoneel
"""

# CS585 - PA1

import numpy as np
import cv2

# Grascaling Image
def convert2grayscale(img):
    imageArray = np.array(img)
    for i in imageArray:
        for j in i:
            gray = int(j[2] * 0.2126 + j[1] * 0.7152 + j[0] * 0.0722)
            j[0] = gray
            j[1] = gray
            j[2] = gray
        
    return imageArray

# Convert to Negative Image
def convert2negative(img):
    imageArray = np.array(img)
    for i in imageArray:
        for j in i:
            j[0] = 255-j[0]
            j[1] = 255-j[1]
            j[2] = 255-j[2]
        
    return imageArray

# Selective grayscaling images - Keep the blue colour and grayscale other colours.
def convert2grayscaleExceptBlues(img):
    imageArray = np.array(img)
    for i in imageArray:
        for j in i:
            if j[0]>43 and j[0]>j[1] and j[0]>j[2]:
                j[0] = j[0]
                j[1] = j[1]
                j[2] = j[2]
            else:
                gray = int(j[2] * 0.2126 + j[1] * 0.7152 + j[0] * 0.0722)
                j[0] = gray
                j[1] = gray
                j[2] = gray
        
    return imageArray

# Change imageName to test different images.
imageName = 'Design_01.jpg'

originalImg = cv2.imread(imageName)
grayscaleImage = convert2grayscale(originalImg)
negativeImage = convert2negative(originalImg)
blueOnlyGrayscaleImage = convert2grayscaleExceptBlues(originalImg)
  
# Uncomment/Comment to show/not show the images after conversion.
# cv2.imshow('Original Image',originalImg)        
# cv2.imshow('Grayscale Image',grayscaleImage)
# cv2.imshow('Negative Image',negativeImage)
# cv2.imshow('Blue Grayscale Image',blueOnlyGrayscaleImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Uncomment/Comment to generate/not generate JPG files after conversion.
cv2.imwrite('Grayscale_'+imageName,grayscaleImage)
cv2.imwrite('Negative_'+imageName,negativeImage)
cv2.imwrite('Blue_Only_Grayscale_'+imageName,blueOnlyGrayscaleImage)
print('Done!')

