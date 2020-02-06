from moviepy.editor import VideoFileClip, concatenate_videoclips
import os, sys

i = 0
video_clips = []

root = "./vid/INSERT_FOOTAGE_HERE" #path to DAY FOLDER
day_list = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
print(day_list)

# import os
# for root, dirs, files in os.walk(top, topdown=False):
#     for name in dirs:
#         print (os.path.join(root, name))
#
for day_folder in day_list:
      day_root = root + "/" + day_folder
      day_dirlist = [ item for item in os.listdir(day_root) if os.path.isdir(os.path.join(day_root, item)) ]
      print(day_dirlist)
      for hour_folder in day_dirlist:
          hour_root = day_root + "/" + hour_folder
          minute_list = [ item for item in os.listdir(hour_root) ]
          minute_list.sort()
          print(minute_list)
          for minute_video in minute_list:
              clip = VideoFileClip(hour_root + "/" + minute_video)
              video_clips.append(clip)

final_clip = concatenate_videoclips(video_clips)
final_clip.write_videofile("my_concatenation.mp4")
#     minute_folder = os.listdir(path + "/" + day_folder)
#     for minute_folder in day_folder:
#             print(minute_folder)
#             print("done")
#     print("finished")
#     clip = VideoFileClip(path + )
# for folder in folder:
#
# clip1 = VideoFileClip('./vid/47.mp4')
# clip2 = VideoFileClip('./vid/best-upward-bees.mp4')
# final_clip = concatenate_videoclips([clip1,clip2])
# final_clip.write_videofile("my_concatenation.mp4")
