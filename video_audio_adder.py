from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(video_path, audio_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        video_clip = video_clip.set_audio(audio_clip)

        output_path = 'output_with_audio.mp4'
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        print(f"Audio successfully added and saved as '{output_path}'.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        video_clip.close()
        audio_clip.close()
