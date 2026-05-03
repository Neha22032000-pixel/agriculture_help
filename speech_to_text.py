import whisper

model = whisper.load_model("base")  # small, fast enough

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
