import numpy as np
import cv2 as cv

cap = cv.VideoCapture('test1.mp4')

while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    #turn the pixel red
    high_brown = np.array([0, 0, 0])
    low_brown = np.array([100, 100, 100])

    mask = cv.inRange(hsv, high_brown, low_brown)

    brown = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow('frame', hsv)
    cv.imshow('mask', brown)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
