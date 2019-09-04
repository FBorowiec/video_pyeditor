from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

def trim_video(video, video_name):
  start_t = int(input("start time (sec): "))
  end_t = int(input("end time (sec): "))
  ffmpeg_extract_subclip(video, start_t, end_t, targetname="videos/" + video_name + "_trimmed.mp4")
  return "Video trimmed successfully!"

#  start_t = int(input("start time (sec): "))
#  end_t = int(input("end time (sec): "))
#  clip = VideoFileClip(video)
#  new_clip = clip.subclip(start_t, end_t)
#  video_rotated = os.getcwd() + '/videos/' + video_name + '_trimmed.mp4'
#  new_clip.write_videofile(video_rotated)
#  return "Video trimmed successfully!"