import cv2 as cv

# img = cv.imread('/home/sumiru/Downloads/_ (1).jpeg')
# cv.imshow('photo', img)
# cv.waitKey(0)

capture = cv.VideoCapture('/home/sumiru/Downloads/v09044940000bp4gi9bkh7bov0si4a6g.mp4')

def rescaleFrame(frame, scale=0.75):
    # Images, Video and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resize_img = rescaleFrame(img)
# cv.imshow('Resized Image', resize_img)

# def changeRes(width, height):
#     # Live Video
#     capture.set(3, width)
#     capture.set(4, height)

while True:
    isTrue, frame = capture.read()
    if isTrue==True:
        frame_resized = rescaleFrame(frame, scale=0.5)

        cv.imshow('Video', frame)
        cv.imshow('resizedVideo', frame_resized)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break
capture.release()
cv.destroyAllWindows()