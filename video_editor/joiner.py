import subprocess
import sys
import os

def join_videos(video, video_name):
    second_video_name = input("Please enter name of second video to be appended: ")
    second_video = os.getcwd() + '/videos/' + second_video_name + '.mp4'
    cmd1 = "ffmpeg -i \"" + video + "\" -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts && ffmpeg -i \"" + second_video + "\" -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts"
    cmd2 = "ffmpeg -i \"concat:temp1.ts|temp2.ts\" -c copy -bsf:a aac_adtstoasc " + os.getcwd() + '/videos/' + video_name + '_joined.mp4'
    returned_value = subprocess.call(cmd1, shell=True)
    returned_value = subprocess.call(cmd2, shell=True)
    return "Videos concatenated successfully!"
