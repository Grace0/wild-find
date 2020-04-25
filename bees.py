import cv2 as cv
import numpy as np
import imutils
import time
from beepipe import BeePipeline

pipe = BeePipeline()

bee_count = 0

def detect_bees():
    None

cap = cv.VideoCapture('./vid/best-upward-bees-cropped.mp4')

ret, frame1 = cap.read() #get first frame
pipe.process(frame1) #process first frame
frame1_rgb = pipe.rgb_threshold_output

while cap.isOpened():

    ret, frame = cap.read()
    unprocessed = frame
    pipe.process(frame)
    frame_rgb = pipe.rgb_threshold_output

    diff = cv.absdiff(frame_rgb, frame1_rgb)
    thresh = cv.threshold(diff, 100, 255, cv.THRESH_BINARY)[1]

    two_images = np.hstack((frame_rgb, thresh))
    cv.imshow('unprocessed', unprocessed)
    cv.imshow('frame', two_images)

    # cv.imshow('frame1', frame1_rgb)
    # cv.imshow('frame', frame_rgb)

    if cv.waitKey(1) == ord('q'):
         break
               # contours = pipe.filter_contours_output
               # frame = cv.drawContours(frame, contours, -1, (0, 0, 255), 3)
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # diff = cv.absdiff(gray, frame1)
    # thresh = cv.threshold(diff, 100, 255, cv.THRESH_BINARY)[1]

#    blur = cv.GaussianBlur(gray, (5, 5), 0)
#    _, thresh = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
#    dilated = cv.dilate(thresh, None, iterations=3)
#    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#    cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # cv.imshow('thresh', thresh)
    # #cv.imshow('diff', diff)
    # cv.imshow('gray', thresh)
    #two_images = np.hstack(thresh))


cap.release()
cv.destroyAllWindows()
