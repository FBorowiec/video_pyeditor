#!/usr/bin/env python3
import os

from video_editor import formatter
from video_editor import rotator
from video_editor import trimmer
from video_editor import resizer
from video_editor import metadata_editor

def main():
  print(" VIDEO EDITOR 0.1")
  i1 = int(input("  1. Rotate a video\n\
  2. Trim a video\n\
  3. Change video aspect\n\
  4. Resize a video\n\
  5. Edit date of a video \n\
  [1/2/3/4/5]: "))
  
  video_name = input("Please enter your video name: ")
  video = os.getcwd() + '/videos/' + video_name
  print(video + " is being processed...")
  
  if (i1 == 1):
    rotator.rotate_video(video)
  elif (i1 == 2):
    trimmer.trim_video(video)
  elif (i1 == 3):
    formatter.format(video)
  elif (i1 == 4):
    print("Not supported (yet)...")
    #resizer.resize_video(video)
  elif (i1 == 5):
    metadata_editor.date_changer(video)
  else:
    print("Invalid choice!")

if (__name__ == '__main__'):
  main()
