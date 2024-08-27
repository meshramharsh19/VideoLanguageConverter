import os
import speech_recognition as sr
from audio_splitter import split_audio

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    full_text = ""

    segments = split_audio(audio_file)
    for segment in segments:
        try:
            with sr.AudioFile(segment) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                full_text += text + " "
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand a segment.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        os.remove(segment)

    return full_text.strip()
