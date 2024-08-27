from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_file, audio_file):
    try:
        video = VideoFileClip(video_file)  # Loads the video files
        audio = video.audio  # Extracts the audio from the video.
        audio.write_audiofile(audio_file)  # Saving the audio to file
        audio.close()
        video.close()
        print(f"Processing...")
    except Exception as e:
        print(f"An error occurred while converting video to audio: {e}")
