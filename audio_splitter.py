from pydub import AudioSegment

def split_audio(audio_file, segment_length=30):
    """Split audio into segments of `segment_length` seconds."""
    audio = AudioSegment.from_file(audio_file)
    length_ms = len(audio)
    segments = []

    for i in range(0, length_ms, segment_length * 1000):
        segment = audio[i:i + segment_length * 1000]
        segment_file = f"segment_{i // 1000}.wav"
        segment.export(segment_file, format="wav")
        segments.append(segment_file)

    return segments
