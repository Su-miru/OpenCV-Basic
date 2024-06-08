import cv2 as cv
import numpy as np

black = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Black', black)

# Paint the image a certain color
# black[200:300, 300:400] = 0,0,255
# cv.imshow('Red',black)

# Draw a rectangle
cv.rectangle(black, (0,0), (black.shape[1]//2,black.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', black)

# Draw a circle
cv.circle(black, (black.shape[1]//2,black.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', black)

# Draw a line
cv.line(black, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', black)

# Write Text
cv.putText(black, 'Drawing Nothing', (125,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,50,225), thickness=2)
cv.imshow('Text', black)

# img = cv.imread('/home/sumiru/Downloads/85243351_p1_master1200.jpg')
# cv.imshow('Image', img)

cv.waitKey(0)