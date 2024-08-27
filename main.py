from video_converter import convert_video_to_audio
from transcriber import transcribe_audio
from translator import translate_text
from text_to_speech import text_to_speech
from video_muter import mute_video
from video_audio_adder import add_audio_to_video

# List of supported languages
supported_languages = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali',
    # Add the rest of the languages here...
}


def main():
    while True:
        print("\nChoose an option:")
        print("1. Convert and Translate Video")
        print("2. Mute Video")
        print("3. Add Audio to Muted Video")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            video_file = input("Enter the path to the video file (e.g., 'input_video.mp4'): ")
            audio_file = "output_audio.wav"
            convert_video_to_audio(video_file, audio_file)

            text = transcribe_audio(audio_file)
            if text:
                print(f"Transcribed text: {text}")

                # Save transcribed text to a file
                with open("transcribed_text.txt", "w", encoding="utf-8") as file:
                    file.write(text)
                print("Transcribed text has been saved to transcribed_text.txt")

                print("Supported languages:")
                for key, value in supported_languages.items():
                    print(f"{key}: {value}")

                target_language = input("Enter the target language code (e.g., 'es' for Spanish, 'fr' for French): ")
                if target_language in supported_languages:
                    translated_text = translate_text(text, target_language)
                    if translated_text:
                        print(f"Translated text: {translated_text}")
                        translated_audio_file = "translated_audio.mp3"
                        text_to_speech(translated_text, target_language, translated_audio_file)

                        # Save translated text to a file
                        translated_text_file = f"translated_text_{target_language}.txt"
                        with open(translated_text_file, "w", encoding="utf-8") as file:
                            file.write(translated_text)
                        print(f"Translated text has been saved to {translated_text_file}")
                else:
                    print("Unsupported language code entered.")
            else:
                print("Transcription failed. No text to translate.")

        elif choice == '2':
            video_file = input("Enter the path to the video file (MP4 format): ")
            mute_video(video_file)

        elif choice == '3':
            video_path = input("Enter path to the muted MP4 video file: ")
            audio_path = input("Enter path to the MP3 audio file: ")
            add_audio_to_video(video_path, audio_path)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
