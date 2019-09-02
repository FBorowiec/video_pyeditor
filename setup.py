#!/usr/bin/env python3

import sys
import imageio
import subprocess

#pip install -r requirements.txt
#pip install --trusted-host pypi.python.org moviepy
#imageio.plugins.ffmpeg.download()

subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
subprocess.call(['pip', 'install', '--trusted-host', 'pypi.python.org', 'moviepy'])
subprocess.call(['pip', 'install', 'imageio-ffmpeg'])
