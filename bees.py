import cv2 as cv
import numpy as np
import imutils
import time
from beepipe import BeePipeline
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show

pipe = BeePipeline()

x = []
y = []
bee_count = 0
frame_count = 0

def detect_bees():
    None

cap = cv.VideoCapture('./vid/best-upward-bees-sky.mp4')

ret, frame1 = cap.read() #get first frame
pipe.process(frame1) #process first frame
frame1_rgb = pipe.rgb_threshold_output

while cap.isOpened():

    frame_count += 1

    ret, frame = cap.read()
    unprocessed = frame
    pipe.process(frame)
    frame_rgb = pipe.rgb_threshold_output

    diff = cv.absdiff(frame_rgb, frame1_rgb)
    thresh = cv.threshold(diff, 200, 255, cv.THRESH_BINARY)[1]

    pipe.process_diff(thresh)
    thresh_contours = pipe.filter_contours_output
    cv.drawContours(unprocessed, thresh_contours, -1, (255, 255, 255), 2)
#    (pipe.find_contours_output) = pipe.__find_contours(pipe.__find_contours_input, pipe.__find_contours_external_only)
    # Step Filter_Contours0:
    # self.__filter_contours_contours = self.find_contours_output
    # (self.filter_contours_output) = self.__filter_contours(self.__filter_contours_contours, self.__filter_contours_min_area, self.__filter_contours_min_perimeter, self.__filter_contours_min_width, self.__filter_contours_max_width, self.__filter_contours_min_height, self.__filter_contours_max_height, self.__filter_contours_solidity, self.__filter_contours_max_vertices, self.__filter_contours_min_vertices, self.__filter_contours_min_ratio, self.__filter_contours_max_ratio)
    cv.putText(unprocessed, str(len(pipe.filter_contours_output)), (50,100), cv.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

#    plt.axis([0,100,0,10])


    x.append(frame_count)
    y.append(str(len(pipe.filter_contours_output)))
    # #two_images = np.hstack((thresh, thresh_contours))
    # plot(x, y)
    # draw()
    # show()
    # # plt.ylabel('BEE COUNT')
    # # plt.xlabel('FRAME NUMBER')

    # # plt.show() #update while showing?!
    plt.autoscale(enable=True, axis='both', tight=None)
    plt.plot(x, y, color='black', linewidth=2, markersize=2)
    plt.draw()
    plt.pause(0.001)

    cv.imshow('unprocessed', unprocessed)
    #cv.imshow('frame', two_images)

    # cv.imshow('frame1', frame1_rgb)
    # cv.imshow('frame', frame_rgb)

    time.sleep(0.1)


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
