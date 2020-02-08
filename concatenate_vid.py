from moviepy.editor import VideoFileClip, concatenate_videoclips
import os, sys

video_clips = []

root = "./vid/INSERT_FOOTAGE_HERE" #path to DAY FOLDER
save_path = "./concated_vid/"

day_list = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
day_list.sort()
print(day_list)

for day_folder in day_list:
      day_root = root + "/" + day_folder
      day_dirlist = [ item for item in os.listdir(day_root) if os.path.isdir(os.path.join(day_root, item)) ]
      day_dirlist.sort()
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
final_clip.write_videofile(day_folder + "_" + hour_folder + ".mp4")
