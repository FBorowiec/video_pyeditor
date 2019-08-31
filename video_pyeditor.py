#!/usr/bin/env python3
import os

from video_editor import formatter
from video_editor import rotator
from video_editor import trimmer
from video_editor import resizer

def main():
  print(" VIDEO EDITOR 0.1")
  i1 = int(input("  1. Rotate a video\n\
  2. Trim a video\n\
  3. Change video aspect\n\
  [1/2/3]: "))
  video_name = input("Please enter your video name: ")
  video = os.getcwd() + '/videos/' + video_name
  print(video + " is being processed...")
  if (i1 == 1):
    angle = ("Please enter rotation value [90, 180, -90]: ")
    print("Not supported (yet)...")
    #rotator.rotate_video(video, angle)
  elif (i1 == 2):
    start_t = int(input("start time (sec): "))
    end_t = int(input("end time (sec): "))
    trimmer.trim_video(video, start_t, end_t)
  elif (i1 == 3):
    aspect = input("Please choose aspect: [4:3, 16:9]: ")
    formatter.format(video, aspect)
  elif (i1 == 4):
    size = int(input("Please choose size: [720, 1080]: "))
    size_tuple = (size, size/(16/9))
    print("Not supported (yet)...")
    #resizer.resize_video(video, size_tuple)

if (__name__ == '__main__'):
  main()
