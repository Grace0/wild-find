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
frame_count = 0

def detect_bees():
    None

cap = cv.VideoCapture('./vid/best-upward-bees-sky.mp4')

ret, frame1 = cap.read() #get first frame
pipe.process(frame1) #process first frame
frame1_rgb = pipe.rgb_threshold_output

fig = plt.figure() #figsize=(4,13
plot = fig.add_subplot(111)

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

    x.append(frame_count)
    y.append(str(len(pipe.filter_contours_output)))
    plot.plot(x, y, color='red', linewidth=1)
    plt.draw()
    plt.pause(.001)
#    fig.canvas.draw()

    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

#    resized = cv.resize(data, (748, 1280), interpolation = cv.INTER_AREA)

    two_images = np.vstack((unprocessed, data))
    cv.imshow('BEE COUNT', two_images)

    time.sleep(0.1)

    if cv.waitKey(1) == ord('q'):
         break


cap.release()
cv.destroyAllWindows()
