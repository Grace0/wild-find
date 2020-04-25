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
contours = pipe.filter_contours_output #get processed contours for first frame
frame1 = cv.drawContours(frame1, contours, -1, (0, 0, 255), 3) #show processed contours for first frame

while cap.isOpened():

        #print("shape: " + str(frame.ndim) + " shape: " + str(frame.shape))

    # frame1 = imutils.resize(frame1, width=600)
    # frame2 = imutils.resize(frame2, width=600)
     ret, frame = cap.read()
     pipe.process(frame)
     contours = pipe.filter_contours_output
     frame = cv.drawContours(frame, contours, -1, (0, 0, 255), 3)

     cv.imshow('frame1', frame1)
     cv.imshow('frame', frame)

     if cv.waitKey(1) == ord('q'):
          break
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
