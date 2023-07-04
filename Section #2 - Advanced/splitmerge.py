import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Images/boston.jpg')
img = cv.resize(img , (500 , 350) , interpolation=cv.INTER_CUBIC)
cv.imshow('Boston' , img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img);

blue = cv.merge([b,blank , blank])
green = cv.merge([blank, g , blank])
red = cv.merge([blank , blank , r])

cv.imshow('Blue' , b)
cv.imshow('Green' , g)
cv.imshow('Red' , r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged' , merged)

cv.imshow('Blue_merged' , blue)
cv.imshow('Green_merged' , green)
cv.imshow('Red_merged' , red)


cv.waitKey(0)