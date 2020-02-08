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
    #blurred = cv.GaussianBlur(frame, (11, 11), 0)

    greenLower = np.array([0, 100, 0], dtype="uint8") #68, 230, 38 - 28, 220, 58
    greenUpper = np.array([100, 255, 100], dtype="uint8") #-48, 240, 78
#    pts = deque(maxlen=args["buffer"])

	# cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	# 	cv2.CHAIN_APPROX_SIMPLE)
	# cnts = imutils.grab_contours(cnts)
	# center = None

    mask = cv.inRange(frame, greenLower, greenUpper)
    output = cv.bitwise_and(frame, frame, mask = mask)

    #_,threshold = cv.threshold(gray, 110, 255, cv.THRESH_BINARY)
    #contours,_=cv.findContours(threshold, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('frame', np.hstack([frame, output]))

    # for cnt in contours:
    #     approx = cv.approxPolyDP(cnt,0.01*cv.arcLength(cnt,True),True)
    #     print(len(approx))
    #     if len(approx)==4:
    #         print("quadrilateral")
    #         cv.drawContours(frame,[cnt],0,(0,0,255),-1)
    #     cv.imshow('conts', frame)

def detect_movement():
    frame1 = imutils.resize(frame1, width=600)
    frame2 = imutils.resize(frame2, width=600)
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    _,threshold = cv.threshold(img, 110, 255, cv.THRESH_BINARY)
    contours,_=cv.findContours(threshold, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


while cap.isOpened():
    detect_green_boxes()

#     frame1 = imutils.resize(frame1, width=600)
#     frame2 = imutils.resize(frame2, width=600)
#     diff = cv.absdiff(frame1, frame2)
#     gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
#
#     cv.imshow('frame1', frame1)
#     cv.imshow('diff', diff)
#
#     frame1 = frame2 #current becomes old
#     ret, frame2 = cap.read() #new
#
    time.sleep(0.1)
#
    if cv.waitKey(1) == ord('q'):
         break

cap.release()
cv.destroyAllWindows()
