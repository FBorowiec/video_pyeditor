from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_video(video, targetname="videos/video_trimmed.mp4"):
  start_t = int(input("start time (sec): "))
  end_t = int(input("end time (sec): "))
  ffmpeg_extract_subclip(video, start_t, end_t, targetname=targetname)
  return "Video trimmed successfully!"


#myclip = VideoFileClip("some_video.avi")
#print (myclip.fps) # prints for instance '30'
## Now cut the clip between t=10 and 25 secs. This conserves the fps.
#myclip2 = myclip.subclip(10, 25)