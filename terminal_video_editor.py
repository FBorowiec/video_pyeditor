from lib.parser import parse_arguments
from lib.video_editor_lib import VideoEditor


def interface():
    args = parse_arguments()
    video_editor = VideoEditor(args.video_path)
    video_editor.print()

    if args.rotate:
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
        print(
            "\nWelcome to the Terminal Video Editor!\n\n"
            "Please provide a valid argument option:\n"
            "--rotate\n"
            "--trim\n"
            "--modify_aspect\n"
            "--resize\n"
            "--change_date\n"
            "--concatenate_videos\n"
            "--crop\n"
            "--desktop_record\n"
        )


if __name__ == "__main__":
    interface()
