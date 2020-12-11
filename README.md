# **Script for basic video editing operations**

This is my video editing tool I use for simple operations on videos.

The script allows you to:

- trim the length of a video
- change the format of the video
- rotate a video
- record your desktop
- change video metadata
- modify video aspect
- resize a video
- concatenate more videos
- crop a video

## How to run the code locally with *Bazel* already installed on host

First, you need to instal ```ffmpeg```:

```bash
sudo apt install ffmpeg
```

### Bazel installation

[Install Bazel](https://docs.bazel.build/versions/master/install.html)

Once you have successfully installed *Bazel* you can run the code using:

```bash
bazel run //:video_pyeditor -- --video_path=/path/to/my_video.mp4 --trim
```

## Run the code inside a container

You can use my following Docker image to instantiate a container locally with Ubuntu and Bazel already installed:

```bash
docker run -it --rm framaxwlad/ubuntu_dev:latest
```

There you can simply clone the repository:

```bash
git clone https://github.com/FBorowiec/video_pyeditor.git
apt update && apt install -y ffmpeg
cd video_pyeditor/
```

And use the aforementioned commands to run the program:

```bash
bazel run //:video_pyeditor -- --video_path=/path/to/my_video.mp4 --trim
```

You might want to use the `mount volume` flag `-v` to the folder containing the video ex: -v `~/Videos:/home`. Then running the script with a video under `~/Videos` on host would look like:

```bash
docker run -it --rm -v ~/Videos:/home framaxwlad/ubuntu_dev:latest

git clone https://github.com/FBorowiec/video_pyeditor.git
apt update && apt install -y ffmpeg
cd video_pyeditor/
bazel run //:video_pyeditor -- --video_path=/home/my_video.mp4 --trim
```
