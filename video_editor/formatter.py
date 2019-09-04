import subprocess
import sys

def format(video, video_name):
  aspect = input("Please choose aspect: [16:10, 16:9, 4:3, 3:2, 1:1]: ")
  cmd = "ffmpeg -i \"" + video + "\" -c copy -aspect " + aspect + " \"videos/" + video_name + "_formatted.mp4\""
  returned_value = subprocess.call(cmd, shell=True)
  return "Video formatted successfully!"