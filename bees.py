import cv2 as cv
import numpy as np
import imutils
import time
from beepipe import BeePipeline
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show

from moviepy.editor import ImageSequenceClip

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

fig = plt.figure()
plot = fig.add_subplot(411)
plot.autoscale(enable=True, axis='both', tight=None)

frame_array = []

while frame_count < 820: #cap.isOpened()

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

    cv.putText(unprocessed, str(len(pipe.filter_contours_output)), (50,100), cv.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    x.append(frame_count)
    y.append(str(len(pipe.filter_contours_output)))

    if len(y) == 48: #first bee counts go 1,3,2; but new numbers are added to the plot axes in order of their appearance; insert 2 as a temporary fix
        y[47] = 2

    if len(y) == 505: #first bee counts go 1,3,2; but new numbers are added to the plot axes in order of their appearance; insert 2 as a temporary fix
        y[504] = 5

    plot.plot(x, y, color='red', linewidth=1)
    plt.draw()
    plt.pause(.001)

    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    two_images = np.vstack((unprocessed, data))
    cropped_image = two_images[0:1200, 0:1280]
    cv.imshow('BEE COUNT', cropped_image)

    cropped_image_bgr = cv.cvtColor(cropped_image, cv.COLOR_RGB2BGR)
    frame_array.append(cropped_image_bgr)

    #time.sleep(0.1) #approx correct timing?

    if cv.waitKey(1) == ord('q'):
         break

cap.release()
cv.destroyAllWindows()

pathOut = 'bee_counter.mp4'
fps = 0.5
size = (1200, 1280)

clip = ImageSequenceClip(frame_array, fps=15)
clip.write_videofile("bee_counter.mp4",fps=15)
