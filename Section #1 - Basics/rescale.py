import cv2 as cv

############ read images ##############
def rescaleFrame(frame , scale = 0.75):
    # images , videos & camera video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

def changeRes(width , height):
    # only for camera videos
    capture.set(3 , width)
    capture.set(4 , height)


img = rescaleFrame(cv.imread('../Resources/Images/dog.jpg') , 0.2)


cv.imshow('cat',img) 


#  cv.waitKey(0) #wait for key from users for infinite time


######### Reading videos  ###############

capture = cv.VideoCapture('../Resources/Videos/dogplay.mp4')

# capture = cv.VideoCapture(0)  # for video taken from camera

while True:
    isTrue, frame  = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video' , frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): # close after some time '20' or after pressing letter 'd'
        break

capture.release()
cv.destroyAllWindows()