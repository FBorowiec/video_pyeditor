

import subprocess
import sys

def date_changer(video):
  date = input("Please choose a date: \"2015-12-25T12:34:56:\"")
  cmd = "ffmpeg -i \"" + video + "\" -c copy -map 0 -metadata creation_time=\"" + date + "\" \"videos/video_metadated.mp4\""
  returned_value = subprocess.call(cmd, shell=True)
  return "Video's date edited successfully!"
