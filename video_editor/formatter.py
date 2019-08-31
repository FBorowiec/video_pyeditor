import subprocess
import sys

def format(video, aspect):
  cmd = "ffmpeg -i \"" + video + "\" -c copy -aspect " + aspect + " \"videos/video_formatted.mp4\""
  returned_value = subprocess.call(cmd, shell=True)
  return "Video formatted successfully!"