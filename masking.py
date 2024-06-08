import cv2 as cv
import numpy as np

img = cv.imread('/home/sumiru/Downloads/85243351_p1_master1200.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

#########

circle = cv.circle(blank.copy(), (75,200), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (75,100), (250,300), 255, -1)
mask_1 = cv.bitwise_and(circle, rectangle)
masked_1 = cv.bitwise_and(img, img, mask=mask_1)
cv.imshow('Masked 2', masked_1)

###########

cv.waitKey(0)