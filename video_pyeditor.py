#!/usr/bin/env python3
import os

from video_editor import formatter
from video_editor import rotator
from video_editor import trimmer
from video_editor import resizer
from video_editor import metadata_editor
from video_editor import joiner

def main():
  print(" VIDEO EDITOR")
  i1 = int(input("  1. Rotate a video\n\
  2. Trim a video\n\
  3. Change video aspect\n\
  4. Resize a video\n\
  5. Edit date of a video \n\
  6. Concatenate two videos \n\
  [1/2/3/4/5/6]: "))
  
  video_name = input("Please enter your mp4 video name (without the extension): ")
  video = os.getcwd() + '/videos/' + video_name + '.mp4'
  print(video + " is being processed...")
  
  if (i1 == 1):
    rotator.rotate_video(video, video_name=video_name)
  elif (i1 == 2):
    trimmer.trim_video(video, video_name=video_name)
  elif (i1 == 3):
    formatter.format(video, video_name=video_name)
  elif (i1 == 4):
    resizer.resize_video(video, video_name=video_name)
  elif (i1 == 5):
    metadata_editor.date_changer(video, video_name=video_name)
  elif (i1 == 6):
    joiner.join_videos(video, video_name=video_name)
  else:
    print("Invalid choice!")

if (__name__ == '__main__'):
  main()
