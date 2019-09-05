import subprocess
import sys
import os
import cv2

def join_videos(video, video_name):

    vid1 = cv2.VideoCapture(video)
    height_v1 = vid1.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width_v1 = vid1.get(cv2.CAP_PROP_FRAME_WIDTH)
    first_video_resolution = [width_v1, height_v1]

    second_video_name = input("Please enter name of second video to be appended: ")
    second_video = os.getcwd() + '/videos/' + second_video_name + '.mp4'
    vid2 = cv2.VideoCapture(second_video)
    height_v2 = vid2.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width_v2 = vid2.get(cv2.CAP_PROP_FRAME_WIDTH)
    second_video_resolution = [width_v2, height_v2]
    
    print(f"Resolution of first video:{int(first_video_resolution[0])}x{int(first_video_resolution[1])}\nResolution of second video: {int(second_video_resolution[0])}x{int(second_video_resolution[1])}")
    if (first_video_resolution != second_video_resolution):
        print ("Error: Videos do not have the same resolution! Consider changing the resolution of one of your videos to match the other.")
        return 0
    
    cmd3 = "ffmpeg -i \"" + video + "\" -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts && ffmpeg -i \"" + second_video + "\" -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts"
    cmd4 = "ffmpeg -i \"concat:temp1.ts|temp2.ts\" -c copy -bsf:a aac_adtstoasc " + os.getcwd() + '/videos/' + video_name + '_joined.mp4'
    returned_value = subprocess.call(cmd3, shell=True)
    returned_value = subprocess.call(cmd4, shell=True)
    cmd5 = "rm temp*"
    returned_value = subprocess.call(cmd5, shell=True)
    return "Videos concatenated successfully!"
