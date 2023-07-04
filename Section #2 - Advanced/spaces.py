import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Resources/Images/boston.jpg')
img = cv.resize(img , (500 , 320) , interpolation=cv.INTER_CUBIC)
cv.imshow('Boston' , img);

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# BGR to HSV
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('HSV' , hsv)

#BGR to L*a*b
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('LAB' , lab)

# BGR to RGB
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
cv.imshow('RGB' , rgb)


# Grayscale to BGR
gray_bgr = cv.cvtColor(gray , cv.COLOR_GRAY2BGR)  # why this is not working ?
cv.imshow('Gray --> BGR' , gray_bgr)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv , cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR' , hsv_bgr)

# L*a*b to BGR
lab_bgr = cv.cvtColor(lab , cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR' , lab_bgr)

# RGB to BGR
rgb_bgr = cv.cvtColor(rgb , cv.COLOR_BGR2RGB)
cv.imshow('RGB --> BGR' , rgb_bgr)

plt.imshow(rgb) # it inverse the color (RGB -> BGR)

plt.show()

cv.waitKey(0);