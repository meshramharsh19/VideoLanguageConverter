from gtts import gTTS

def text_to_speech(text, language, output_file):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file)
        print(f"Translated audio has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while converting text to speech: {e}")
