import numpy as np
import cv2 as cv
from collections import deque
from imutils.video import VideoStream
import imutils
import time

#in general, not just bees

#write clips of when the green box appears -- clip starts when green box appears and stops when that same one disappears
#write clips of when something moving appears -- clip starts when thing appears and stops when that same thing disappears

cap = cv.VideoCapture('./vid/best-upward-bees.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

def detect_green_boxes():
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    contours,_=cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        print(len(approx))
        if len(approx)==4:
            print("quadrilateral")
            cv2.drawContours(img,[cnt],0,(0,0,255),-1)

def detect_movement():
    frame1 = imutils.resize(frame1, width=600)
    frame2 = imutils.resize(frame2, width=600)
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    contours,_=cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

while cap.isOpened():
    frame1 = imutils.resize(frame1, width=600)
    frame2 = imutils.resize(frame2, width=600)
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    cv.imshow('frame1', frame1)
    cv.imshow('diff', diff)

    frame1 = frame2 #current becomes old
    ret, frame2 = cap.read() #new

    # time.sleep(0.5)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
