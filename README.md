# *Script for basic video editing operations*

The script allows you to:

- trim the length of a video
- change the format of the video
- rotate a video
- record your desktop
- change video metadata
- and more...

## How to run

First, you need to instal ```ffmpeg```:

```sudo apt install ffmpeg```

Then run the video editor with:

```bash
bazel run //:video_pyeditor -- --video_path=/home/fra/Videos/my_video.mp4 --trim
```
