import subprocess
import sys
import os
import cv2

def crop(video, video_name):
    w = input("Please provide width crop value: \n\
    Width of the output video (out_w). It defaults to iw. This expression is evaluated only once during the filter configuration: ")
    w = str(1280 - int(w))
    h = input("Please provide height crop value: \n\
    Height of the output video (out_h). It defaults to ih. This expression is evaluated only once during the filter configuration: ")
    h = str(720 - int(h))
    x = input("Please provide width crop value: \n\
    Horizontal position, in the input video, of the left edge of the output video. It defaults to (in_w-out_w)/2. This expression is evaluated per-frame: ")
    y = input("Please provide y crop value: \n\
    Vertical position, in the input video, of the top edge of the output video. It defaults to (in_h-out_h)/2. This expression is evaluated per-frame: ")
    cmd = "ffmpeg -i \"" + video + "\" -vf \"crop=" + w + ":" + h + ":" + x + ":" + y + "\" " + os.getcwd() + '/videos/' + video_name + '_cropped.mp4'
    returned_value = subprocess.call(cmd, shell=True)
    return "Video cropped successfully!"