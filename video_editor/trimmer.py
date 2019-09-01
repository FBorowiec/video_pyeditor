from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_video(video, targetname="videos/video_trimmed.mp4"):
  start_t = int(input("start time (sec): "))
  end_t = int(input("end time (sec): "))
  ffmpeg_extract_subclip(video, start_t, end_t, targetname=targetname)
  return "Video trimmed successfully!"