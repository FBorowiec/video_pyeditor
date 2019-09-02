import subprocess
import sys

def format(video):
  aspect = input("Please choose aspect: [4:3, 16:9]: ")
  cmd = "ffmpeg -i \"" + video + "\" -c copy -aspect " + aspect + " \"videos/video_formatted.mp4\""
  returned_value = subprocess.call(cmd, shell=True)
  return "Video formatted successfully!"