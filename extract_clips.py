import sys
import shutil
import os

from moviepy.video.io.VideoFileClip import VideoFileClip

# print("vid name:" + str(sys.argv[1]))
# print("start_time:" + str(sys.argv[2]))
# print("end_time:" + str(sys.argv[3]))
# print("output name:" + str(sys.argv[4]))

input_video_path = str(sys.argv[1])
t1 = int(sys.argv[2])
t2 = int(sys.argv[3])
output_video_name = str(sys.argv[4])

output_video_path = "./vid/RPG-0123-0124_PROS/" + str(output_video_name) + ".mp4"

with VideoFileClip(input_video_path) as video:
    new = video.subclip(t1, t2)
    new.write_videofile(output_video_path, audio_codec='aac')
