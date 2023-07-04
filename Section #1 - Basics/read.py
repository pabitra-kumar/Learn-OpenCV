import cv2 as cv

# read images

# img = cv.imread('../Resources/Images/dog.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)



# Reading videos

capture = cv.VideoCapture('../Resources/Videos/dogplay.mp4')

while True:
    isTrue, frame  = capture.read()
    cv.imshow('Video' , frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()