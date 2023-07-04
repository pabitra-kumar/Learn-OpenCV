import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Resources/Images/cat.jpg')
img = cv.resize(img , (500 , 320) , interpolation= cv.INTER_CUBIC)
cv.imshow('cats' , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('Blank' , blank)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray )

circle = cv.circle(blank.copy() , (img.shape[1]//2 + 70 , img.shape[0]//2) , 100 , 255 , -1)
cv.imshow('Circle' , circle)

# mask_circle = cv.bitwise_and(gray , gray , mask=circle)
# cv.imshow("Circular mask" , mask_circle)


#  GrayScale Histogram
# gray_hist = cv.calcHist([gray] , [0] , circle , [256] , [0,256])

# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0 , 256])
# plt.show()

# color Histogram

plt.figure()
plt.title("Colour Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('r' , 'g' , 'b')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i] , circle , [256] , [0,256] )
    plt.plot(hist , color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)