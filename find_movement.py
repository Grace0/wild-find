import numpy as np
import cv2 as cv
from collections import deque
from imutils.video import VideoStream
import imutils
import time
from grip import GripPipeline

pipe = GripPipeline()

img_array = [] #for frames with green boxes

cap = cv.VideoCapture('./vid/47.mp4')
fps = cap.get(cv.CAP_PROP_FPS) #15

ret, frame1 = cap.read()
height, width, layers = frame1.shape #just do this once, for VideoWriter
size = (width,height) #1920, 1080

def detect_green_boxes():
    ret, frame = cap.read()
    pipe.process(frame)
    contours = pipe.find_contours_output
    output = cv.drawContours(frame.copy(), contours, -1, (0, 255, 0), 3)

    print(str(len(contours)))
    if len(contours) > 0: #does return num of contours
        cv.circle(output,(300,240), 63, (0,0,255), -1)
        print("yes")
    else:
        None
    two_images = np.hstack((frame, output))
    cv.imshow('frame', two_images)
# def detect_movement():
#     frame1 = imutils.resize(frame1, width=600)
#     frame2 = imutils.resize(frame2, width=600)
#     diff = cv.absdiff(frame1, frame2)
#     gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
#     _,threshold = cv.threshold(img, 110, 255, cv.THRESH_BINARY)
#     contours,_=cv.findContours(threshold, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


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
