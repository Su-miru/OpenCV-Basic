import cv2 as cv

# --------- READING IMAGES

# img = cv.imread('85243351_p1_master1200.jpg')

# cv.imshow('image', img)

# cv.waitKey(0)

# --------- READING VIDEOS

capture = cv.VideoCapture('/home/sumiru/Downloads/v09044940000bp4gi9bkh7bov0si4a6g.mp4')

while True:
	isTrue, frame = capture.read()
	cv.imshow('Video', frame)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break
capture.release()
cv.destroyAllWindows()