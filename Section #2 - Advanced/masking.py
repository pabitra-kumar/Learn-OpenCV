import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Images/cats.jpg')
img = cv.resize(img , (500 , 320) , interpolation= cv.INTER_CUBIC)
cv.imshow('cats' , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('blank' , blank)

mask = cv.circle(blank.copy() , (img.shape[1]//2 + 70, img.shape[0]//2) , 100 , 255 , -1)
cv.imshow('Mask Circle' , mask)

masked = cv.bitwise_and(img , img , mask=mask)
cv.imshow('Masked Circle Image' , masked)

mask_rect = cv.rectangle(blank.copy() , (img.shape[1]//2, img.shape[0]//2) , (img.shape[1]//2 + 100, img.shape[0]//2 +100) , 255 , -1)
cv.imshow('Mask Rectangle' , mask_rect)

weird_shape = cv.bitwise_and( mask , mask_rect)
cv.imshow('Weird Shape' , weird_shape)

exp = cv.bitwise_and(img , img , mask=weird_shape)
cv.imshow('Weird Shape image' , exp)



masked_rect = cv.bitwise_and(img , img , mask=mask_rect)
cv.imshow('Masked Rectangle Image' , masked_rect)






cv.waitKey(0)