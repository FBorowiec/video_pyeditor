import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description="TERMINAL VIDEO EDITOR")
    parser.add_argument(
        "--video_path", type=Path, help="Absolute path to video", required=True
    )

    editor = parser.add_mutually_exclusive_group()
    editor.add_argument(
        "--rotate", help="Rotate a video", required=False, action="store_true"
    )
    editor.add_argument(
        "--trim", help="Trim a video", required=False, action="store_true"
    )
    editor.add_argument(
        "--modify_aspect",
        help="Change a video aspect",
        required=False,
        action="store_true",
    )
    editor.add_argument("--resize", help="Resize", required=False, action="store_true")
    editor.add_argument(
        "--change_date",
        help="Edit date of a video",
        required=False,
        action="store_true",
    )
    editor.add_argument(
        "--concatenate_videos",
        help="Concatenate two videos",
        required=False,
        action="store_true",
    )
    editor.add_argument(
        "--crop", help="Crop a video", required=False, action="store_true"
    )
    editor.add_argument(
        "--desktop_record", help="Record desktop", required=False, action="store_true"
    )

    return parser.parse_args()
