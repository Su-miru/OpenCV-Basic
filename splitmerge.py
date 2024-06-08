import cv2 as cv
import numpy as np

img = cv.imread('/home/sumiru/Downloads/blue-flowers-22.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue_Color', blue)
cv.imshow('Green_Color', green)
cv.imshow('Red_Color', red)

cv.waitKey(0)