import cv2 as cv
import numpy as np

blank = np.zeros((500 , 500 , 3) , dtype='uint8')

cv.imshow('Blank' , blank)

# 1. paint the entire image with blue color
# blank[:] = 255,0,0
# cv.imshow('Green' , blank)

# 1.1 paint the portion of image with Green
# blank[200:300 , 300:400] = 0,255,0
# cv.imshow('Green' , blank)

# 2. Draw a rectangle
# cv.rectangle(blank , (0,0) , (blank.shape[1]//2 ,blank.shape[0]//2) , (0,0 , 255) , thickness = -1 )
# # thickness = cv.FILLED || -1  || <Any Number>
# cv.imshow('Rectangle' , blank)


# # 3. Draw a circle
# cv.circle(blank , (blank.shape[1]//2 ,blank.shape[0]//2) , 40 , (0,0,0) , thickness = -1)
# cv.imshow('Circle' , blank)

# # 4. Draw a line
# cv.line(blank , (100 , 250) , (300 , 400) , (0,255 , 0) , thickness=3)
# cv.imshow('circle' , blank)

# 5. Write Text
cv.putText(blank , "Hello , My name is Pabi!!!" , (0 , 225) , cv.FONT_HERSHEY_COMPLEX , 1.0 , (0 , 255 , 0) , 2 )
cv.imshow('Text' , blank)


cv.waitKey(0)
