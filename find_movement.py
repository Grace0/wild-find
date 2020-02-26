import numpy as np
import cv2 as cv
from collections import deque
from imutils.video import VideoStream
import imutils
import time

img_array = [] #for frames with green boxes

cap = cv.VideoCapture('./vid/best-upward-bees.mp4')
fps = cap.get(cv.CAP_PROP_FPS) #15

ret, frame1 = cap.read()
height, width, layers = frame1.shape #just do this once, for VideoWriter
size = (width,height) #1920, 1080

def detect_green_boxes():
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    #blurred = cv.GaussianBlur(frame, (11, 11), 0)

    greenLower = np.array([0, 100, 0], dtype="uint8") #68, 230, 38 - 28, 220, 58
    greenUpper = np.array([100, 255, 100], dtype="uint8") #-48, 240, 78

    mask = cv.inRange(frame, greenLower, greenUpper)
    output = cv.bitwise_and(frame, frame, mask = mask)
    edged = cv.Canny(output, 30, 200)

    contours, hierarchy = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#    cnts = cv.findContours(output, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#    cnts = imutils.grab_contours(cnts)
    cv.drawContours(frame, contours, -1, (0, 255, 0), 1)

    #print("contours ", len(cnts))

    #if len(cnts) > 0:
    #    img_array.append(frame)

    #_,threshold = cv.threshold(gray, 110, 255, cv.THRESH_BINARY)
    #contours,_=cv.findContours(threshold, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('frame', np.hstack([frame, output]))



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

# out = cv.VideoWriter('movement.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size)
# for i in range(len(img_array)):
#     out.write(img_array[i])
#
# out.release()
