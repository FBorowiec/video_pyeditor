from moviepy.video.fx.all import rotate
from moviepy.editor import VideoFileClip
import os

def rotate_video(video, video_name):
  angle = int(input(("Please enter rotation value [90, 180, -90]: ")))
  clip = VideoFileClip(video)
  new_clip = rotate(clip, angle, unit='deg', resample='bicubic', expand=True)
  video_rotated = os.getcwd() + '/videos/' + video_name + '_rotated.mp4'
  new_clip.write_videofile(video_rotated)
  return "Video rotated successfully!"
