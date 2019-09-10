#!/usr/bin/env python3

import sys
import subprocess

#pip install -r requirements.txt
#pip install --trusted-host pypi.python.org moviepy
#imageio.plugins.ffmpeg.download()

subprocess.call(['pip3', 'install', 'imageio'])
subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
subprocess.call(['pip3', 'install', '--trusted-host', 'pypi.python.org', 'moviepy'])
subprocess.call(['pip3', 'install', 'imageio-ffmpeg'])
subprocess.call(['pip3', 'install', '--upgrade', 'mss'])
subprocess.call(['pip3', 'install', 'pyscreenshot'])