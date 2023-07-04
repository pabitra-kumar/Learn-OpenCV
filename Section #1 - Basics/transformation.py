import cv2 as cv
import numpy as np

def rescaleFrame(frame , scale = 0.75):
    # images , videos & camera video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

img = cv.imread('../Resources/Images/boston.jpg')

img = rescaleFrame(img , 0.1)

cv.imshow('Boston' , img)

# Translate
def translate(img , x , y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat , dimensions)

# -x --> Left
# -y --> Up
# x --> right
# y --> down

translated = translate(img , -100, 100)
cv.imshow('Translated' , translated)

# Rotation
def rotate(img , angle , roPoint = None):
    (height , width) = img.shape[:2]

    if roPoint is None:
        roPoint = (width//2 , height//2)
    
    rotMat = cv.getRotationMatrix2D(roPoint , angle , 1.0)
    dimensions = (width , height)
    return cv.warpAffine(img , rotMat , dimensions)

# angle --> ant-clock-wise

rotated = rotate(img , -45)
cv.imshow('Rotate' , rotated)

rotated_rotated = rotate(rotated , -45)
cv.imshow('Rotate Rotated' , rotated_rotated) #this is wong practise

rotated_rotated = rotate(img , -90)
cv.imshow('Rotate Rotated' , rotated_rotated) # this is correct

# Resizing
resized = cv.resize(img , (500 , 500) , interpolation = cv.INTER_CUBIC)
cv.imshow('Resize' , resized)

# Fliping
flip = cv.flip(img , 0) # vertical flip
flip = cv.flip(img , 1) # horizontal flip
flip = cv.flip(img , -1) # vertical as well as horizontal flip
cv.imshow('Flip' , flip)

# Cropping
cropped = img[200:400 , 300:400]
cv.imshow('Cropped' , cropped)



cv.waitKey(0)