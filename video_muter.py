import os
from moviepy.editor import VideoFileClip

def mute_video(input_path):
    try:
        clip = VideoFileClip(input_path)

        clip = clip.without_audio()

        output_folder = "mutevideos"
        os.makedirs(output_folder, exist_ok=True)

        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}_muted{ext}")

        clip.write_videofile(output_path)

        print(f"Muted video saved successfully at {output_path}")
    except Exception as e:
        print(f"Error: {e}")
