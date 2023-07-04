import cv2 as cv

img = cv.imread('../Resources/Images/cats.jpg')
img = cv.resize(img , (500 , 350) , cv.INTER_CUBIC)
cv.imshow('cats' , img)

# Averging - Average of sorrounding pixel intensity applied at midddle pixel in a window of kernel size (Ex: (7,7) -> 7X7) throughout the image - increasing blurring with increasing kernel size
average = cv.blur(img , (3,3))
cv.imshow('Average Blur' , average)

# Gaussian Blur - technique is same as averaging, but less blurring than averaging and more realastic
gauss = cv.GaussianBlur(img , (3,3) , 0)
cv.imshow('Gaussian Blur' , gauss)

# Median Blur - like averaging but this take median of pixels around
median = cv.medianBlur(img , 3 )
cv.imshow('Median Blur' , median)

# Bilateral - blurr increases with increasing sigmaColor argument
bilateral = cv.bilateralFilter(img , 10 , 15 , 156)
cv.imshow('Bilateral' , bilateral)



cv.waitKey(0);