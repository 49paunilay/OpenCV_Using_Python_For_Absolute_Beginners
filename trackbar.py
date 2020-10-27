import cv2
import numpy as np

def nothing(x):
    print(x)



cv2.namedWindow('image')

cv2.createTrackbar('B','image',0,170,nothing)
cv2.createTrackbar('G','image',0,170,nothing)
cv2.createTrackbar('R','image',0,170,nothing)

switch = '0:OFF\n 1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    image = cv2.imread("Resources/lena.png")
    cv2.imshow('image',image)

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos(switch,'image')
    if s==0:
        image[:] = 0
    else:
        image[:] = [b,g,r]
    image = cv2.imread("Resources/lena.png")