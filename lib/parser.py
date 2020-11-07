import argparse
from pathlib import Path


class Parser:

  def parse_arguments(self):
    parser = argparse.ArgumentParser(description='VIDEO EDITOR')
    parser.add_argument('--video_path', type=Path, help='Path to video', required=False)
    parser.add_argument('--output_path', type=Path, help='Output path to generated video', required=False)
    parser.add_argument('--rotate', help='Rotate a video', required=False)
    parser.add_argument('--trim', help='Trim a video', required=False)
    parser.add_argument('--modify_aspect', help='Change a video aspect', required=False)
    parser.add_argument('--resize', help='Resize', required=False)
    parser.add_argument('--change_date', help='Edit date of a video', required=False)
    parser.add_argument('--concatenate_videos', help='Concatenate two videos', required=False)
    parser.add_argument('--crop', help='Crop a video', required=False)
    parser.add_argument('--desktop_record', help='Record desktop', required=False)

    return parser.parse_args()
