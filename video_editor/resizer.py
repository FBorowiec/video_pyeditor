from moviepy.video.io.ffmpeg_tools import ffmpeg_resize

def resize_video(video, video_name):
  size = int(input("Please choose size: [360, 720, 1080, 2160]: "))
  size_tuple = (size*(16/9), size)
  print("resizing video...")
  ffmpeg_resize(video, output="videos/" + video_name + "_resized.mp4", size=size_tuple)
  return "Video resized successfully!"