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
    #print("shape: " + str(frame.ndim) + " shape: " + str(frame.shape))
    output = cv.drawContours(pipe.resize_image_output, contours, -1, (0, 0, 255), 3) #BGR

    print("cnt: " + str(len(contours)))
    if len(contours) > 0: #does return num of contours
        cv.circle(output,(300,240), 63, (0,0,255), -1)
        print("yes")
    else:
        None
    two_images = np.hstack((pipe.resize_image_output, output))
    cv.imshow('frame', two_images)


while cap.isOpened():
    detect_green_boxes()

    time.sleep(0.3)

    if cv.waitKey(1) == ord('q'):
         break

cap.release()
cv.destroyAllWindows()

# out = cv.VideoWriter('movement.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size)
# for i in range(len(img_array)):
#     out.write(img_array[i])
#
# out.release()
