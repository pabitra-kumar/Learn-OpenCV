import cv2 as cv
import os

def rescaleFrame(frame , scale = 0.75):
    # images , videos & camera video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

img = cv.imread('../Resources/Images/cat.jpg')

img = rescaleFrame(img , 0.5)

cv.imshow('Cat' , img)

# Converting to grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# Blur
blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
cv.imshow('Blur' , blur)

# Edge Cascade
cany = cv.Canny(blur , 125 , 175)
cv.imshow('Edge Cascade' , cany)

# Dilating the Edges
dilated = cv.dilate(cany , (7,7) , iterations = 3 )
cv.imshow('Dilated' , dilated)

# Eroding
eroded = cv.erode(dilated , (7,7) , iterations = 3 )
cv.imshow('Eroded' , eroded)

# Resize
resized = cv.resize(img , (500 , 500) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized' , resized)

# Cropping
cropped = img[50:200 , 200:400]
cv.imshow('Cropped' , cropped)



cv.waitKey(0)