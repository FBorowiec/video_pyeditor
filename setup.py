#!/usr/bin/env python3

import sys

!{sys.executable} -m pip install -r requirements.txt
!{sys.executable} -m pip install --trusted-host pypi.python.org moviepy
imageio.plugins.ffmpeg.download()