import cv2
import numpy as np
import os
import pyscreenshot as pys
import subprocess
import sys

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.ffmpeg_tools import ffmpeg_resize
from moviepy.video.fx.all import rotate


class VideoEditor:

  def __init__(self, video):
    self.video_path = str(video)
    self.video_folder_path, self.video_name = os.path.split(video)


  def crop(self):
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
      cmd = "ffmpeg -i \"" + self.video_path  + "\" -vf \"crop=" + w + ":" + h + ":" + x + ":" + y + "\" " + self.video_path + '_cropped.mp4'
      returned_value = subprocess.call(cmd, shell=True)
      return "Video cropped successfully!" + str(returned_value)


  def format(self):
    aspect = input("Please choose aspect: [16:10, 16:9, 4:3, 3:2, 1:1]: ")
    cmd = "ffmpeg -i \"" + self.video_path + "\" -c copy -aspect " + aspect + " \"" + self.video_path + "_formatted.mp4\""
    returned_value = subprocess.call(cmd, shell=True)
    return "Video formatted successfully!"


  def join_videos(self):

      vid1 = cv2.VideoCapture(self.video_path)
      height_v1 = vid1.get(cv2.CAP_PROP_FRAME_HEIGHT)
      width_v1 = vid1.get(cv2.CAP_PROP_FRAME_WIDTH)
      first_video_resolution = [width_v1, height_v1]

      second_video_name = input("Please enter name of second video to be appended (without the path nor extension): ")
      second_video = os.path.join(self.video_folder_path, second_video_name + '.mp4')
      vid2 = cv2.VideoCapture(second_video)
      height_v2 = vid2.get(cv2.CAP_PROP_FRAME_HEIGHT)
      width_v2 = vid2.get(cv2.CAP_PROP_FRAME_WIDTH)
      second_video_resolution = [width_v2, height_v2]

      print(f"Resolution of first video:{int(first_video_resolution[0])}x{int(first_video_resolution[1])}\nResolution of second video: {int(second_video_resolution[0])}x{int(second_video_resolution[1])}")
      if (first_video_resolution != second_video_resolution):
          print ("Error: Videos do not have the same resolution! Consider changing the resolution of one of your videos to match the other.")
          return 0

      cmd3 = "ffmpeg -i \"" + self.video_path + "\" -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts && ffmpeg -i \"" + second_video + "\" -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts"
      cmd4 = "ffmpeg -i \"concat:temp1.ts|temp2.ts\" -c copy -bsf:a aac_adtstoasc " + self.video_path + '_joined.mp4'
      returned_value = subprocess.call(cmd3, shell=True)
      returned_value = subprocess.call(cmd4, shell=True)
      cmd5 = "rm temp*"
      returned_value = subprocess.call(cmd5, shell=True)
      return "Videos concatenated successfully!"


  def date_changer(self):
    date = input("Please choose a date: \"2015-12-25T12:34:56:\"")
    cmd = "ffmpeg -i \"" + self.video_path + "\" -c copy -map 0 -metadata creation_time=\"" + date + " " + self.video_path + "_dated.mp4\""
    returned_value = subprocess.call(cmd, shell=True)
    return "Video's date edited successfully!" + str(returned_value)


  def screen_record(self):
    forcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(self.video_path + '.mp4', forcc, 5.0, (1920,1080))
    input("Press 'q' to exit while in window mode!\n\
    Press any key to proceed...")
    while True:
      img = pys.grab()
      img_np = np.array(img)
      frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
      cv2.imshow('Screen', frame)
      out.write(frame)
      if cv2.waitKey(20) & 0xFF==ord('q'):
        break

    out.release()
    cv2.destroyAllWindows()

    return None


  def resize_video(self):
    size = int(input("Please choose size: [360, 720, 1080, 2160]: "))
    size_tuple = (size*(16/9), size)
    print("resizing video...")
    print(self.video_path)
    ffmpeg_resize(self.video_path, output=self.video_path + "_resized.mp4", size=size_tuple)
    return "Video resized successfully!"


  def rotate_video(self):
    angle = int(input(("Please enter rotation value [90, 180, -90]: ")))
    clip = VideoFileClip(self.video_path)
    new_clip = rotate(clip, angle, unit='deg', resample='bicubic', expand=True)
    video_rotated = self.video_path + '_rotated.mp4'
    new_clip.write_videofile(video_rotated)
    return "Video rotated successfully!"


  def trim_video(self):
    start_t = int(input("start time (sec): "))
    end_t = int(input("end time (sec): "))
    ffmpeg_extract_subclip(self.video_path, start_t, end_t, targetname=self.video_path + "_trimmed.mp4")
    return "Video trimmed successfully!"
