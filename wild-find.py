import numpy as np
import cv2 as cv
from collections import deque
from imutils.video import VideoStream
import imutils
import time

#BEES

cap = cv.VideoCapture('./vid/best-upward-bees-cropped.mp4')

ret, frame1 = cap.read()
frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

while cap.isOpened():
    # frame1 = imutils.resize(frame1, width=600)
    # frame2 = imutils.resize(frame2, width=600)
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    diff = cv.absdiff(gray, frame1)
    thresh = cv.threshold(diff, 100, 255, cv.THRESH_BINARY)[1]
#    blur = cv.GaussianBlur(gray, (5, 5), 0)
#    _, thresh = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
#    dilated = cv.dilate(thresh, None, iterations=3)
#    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#    cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv.imshow('thresh', thresh)
    # #cv.imshow('diff', diff)
    # cv.imshow('gray', thresh)
    #two_images = np.hstack(thresh))
    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
