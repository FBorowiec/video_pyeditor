from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_video(video, start_t, end_t, targetname="videos/video_trimmed.mp4"):
  ffmpeg_extract_subclip(video, start_t, end_t, targetname=targetname)
  return "Video trimmed successfully!"