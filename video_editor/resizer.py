from moviepy.video.io.ffmpeg_tools import ffmpeg_resize

def resize_video(video, targetname="videos/video_resized.mp4"):
  size = int(input("Please choose size: [720, 1080]: "))
  size_tuple = (size, size/(16/9))
  ffmpeg_resize(video, output=targetname, size=size_tuple)
  return "Video resized successfully!"