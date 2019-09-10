#!/usr/bin/env python3
import os
import json

from video_editor import formatter
from video_editor import rotator
from video_editor import trimmer
from video_editor import resizer
from video_editor import metadata_editor
from video_editor import joiner
from video_editor import cropper
from video_editor import recorder

def interface(input_choice, video, video_name):
  if (input_choice == 1):
    rotator.rotate_video(video, video_name=video_name)
    video_name = video_name + '_rotated'
  elif (input_choice == 2):
    trimmer.trim_video(video, video_name=video_name)
    video_name = video_name + '_trimmed'
  elif (input_choice == 3):
    formatter.format(video, video_name=video_name)
    video_name = video_name + '_formatted'
  elif (input_choice == 4):
    resizer.resize_video(video, video_name=video_name)
    video_name = video_name + '_resized'
  elif (input_choice == 5):
    metadata_editor.date_changer(video, video_name=video_name)
    video_name = video_name + '_dated'
  elif (input_choice == 6):
    joiner.join_videos(video, video_name=video_name)
    video_name = video_name + '_joined'
  elif (input_choice == 7):
    cropper.crop(video, video_name=video_name)
    video_name = video_name + '_cropped'
  elif (input_choice == 8):
    print("Please press 'q' to exit!")
    recorder.screen_record(video_name=video_name)
  else:
    print("Invalid choice!")
  return video_name

def main():
  print(" VIDEO EDITOR")
  
  video_name = input("Please enter your mp4 video name (without the extension): ")
  
  proceed = True
  while (proceed):
    input_choice = int(input("  1. Rotate a video\n\
  2. Trim a video\n\
  3. Change video aspect\n\
  4. Resize a video\n\
  5. Edit date of a video \n\
  6. Concatenate two videos \n\
  7. Crop a video \n\
  8. Record desktop \n\
  [1/2/3/4/5/6/7/8]: "))
    video = os.getcwd() + '/videos/' + video_name + '.mp4'
    print(video + " is being processed...")
    video_name = interface(input_choice, video=video, video_name=video_name)
    proceed = json.loads(input("Do you want to proceed? [True, False]: ").lower())

if (__name__ == '__main__'):
  main()
