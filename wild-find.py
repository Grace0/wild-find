import numpy as np
import cv2 as cv
from collections import deque
from imutils.video import VideoStream
import imutils
import time

#BEES

cap = cv.VideoCapture('./vid/best-upward-bees.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    frame1 = imutils.resize(frame1, width=600)
    frame2 = imutils.resize(frame2, width=600)
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

#    blur = cv.GaussianBlur(gray, (5, 5), 0)
#    _, thresh = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
#    dilated = cv.dilate(thresh, None, iterations=3)
#    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#    cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv.imshow('frame1', frame1)
    cv.imshow('diff', diff)
    cv.imshow('gray', gray)

    frame1 = frame2 #current becomes old
    ret, frame2 = cap.read() #new

    time.sleep(0.5)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
