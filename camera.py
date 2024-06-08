import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('s'):
        break

capture.release()
cv.destroyAllWindows()

