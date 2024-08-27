from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language).text
        return translated_text
    except Exception as e:
        print(f"An error occurred while translating text: {e}")
