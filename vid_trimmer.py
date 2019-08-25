#pip install --trusted-host pypi.python.org moviepy
#imageio.plugins.ffmpeg.download()

import imageio
import os
import subprocess
import sys

if (len(sys.argv) != 4):
    print("Not enough arguments passed!")
    print("The correct command is: python vid_trimmer_py NAME_OF_THE_VIDEO.mp4 START_sec END_sec")
    quit()

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

###########################################
video_name=sys.argv[1]
start_t = float(sys.argv[2]) #s
end_t = float(sys.argv[3]) #s
video_out = sys.argv[1]+"_out.mp4"
###########################################

# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
ffmpeg_extract_subclip(video_name, start_t, end_t, targetname="video_trimmed.mp4")
cmd = "ffmpeg -i \"video_trimmed.mp4\" -c copy -aspect 4:3 \"video_out.mp4\""
returned_value = subprocess.call(cmd, shell=True)
os.remove("video_trimmed.mp4")
