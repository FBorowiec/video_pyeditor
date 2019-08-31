from moviepy.video.io.ffmpeg_tools import ffmpeg_resize

def resize_video(video, size, targetname="videos/video_resized.mp4"):
  ffmpeg_resize(video, output=targetname, size=size)
  return "Video resized successfully!"