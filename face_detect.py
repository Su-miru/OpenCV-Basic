import cv2 as cv

# /home/sumiru/Downloads/person.jpg
# /home/sumiru/Downloads/group1.jpg
# /home/sumiru/Downloads/group2.jpg

img = cv.imread('/home/sumiru/Downloads/person.jpg')

def rescale(frame, scale=0.5):
    height = int(frame.shape[1] * scale)
    width = int(frame.shape[0] * scale)
    dimensions = (height, width)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img0 = rescale(img, 1)
cv.imshow('Image', img0)

gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
print(f'Number of faces found = {len(faces_rect)}')
print(faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img0, (x,y), (x+w,y+h), (0,255,0), 2)
cv.imshow('Detected Faces', img0)

cv.waitKey(0)