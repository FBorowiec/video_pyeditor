import argparse
import os
from pathlib import Path

from lib.parser import Parser
from lib.video_editor_lib import Utils

def interface():
  args = Parser().parse_arguments()
  video_editor = Utils(args.video_path)

  if args.output_path:
    print("do nothing")
  elif args.rotate:
    video_editor.rotate_video()
  elif args.trim:
    video_editor.trim_video()
  elif args.modify_aspect:
    video_editor.format()
  elif args.resize:
    video_editor.resize_video()
  elif args.change_date:
    video_editor.date_changer()
  elif args.concatenate_videos:
    video_editor.join_videos()
  elif args.crop:
    video_editor.crop()
  elif args.desktop_record:
    video_editor.screen_record()
  else:
    print(f"\nWelcome to the Terminal Video Editor!\n\n"
      "Please provide a valid argument option:\n"
        "--video_path\n"
        "--output_path\n\n"
        "--rotate\n"
        "--trim\n"
        "--modify_aspect\n"
        "--resize\n"
        "--change_date\n"
        "--concatenate_videos\n"
        "--crop\n"
        "--desktop_record\n"
      )


def main():

  interface()

if (__name__ == '__main__'):
  main()
