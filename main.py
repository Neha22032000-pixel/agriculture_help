from speech_to_text import transcribe_audio
from image_analysis import analyze_image
from triage_logic import compute_severity
from utils import parse_transcription


def run_pipeline(audio_path, image_path):
    # Step 1: voice → text
    text = transcribe_audio(audio_path)

    # Step 2: extract structured signals
    features = parse_transcription(text)

    # Step 3: image understanding
    image_result = analyze_image(image_path)

    # Step 4: triage decision
    severity = compute_severity(features, image_result["confidence"])

    # Step 5: output
    result = {
        "severity": severity,
        "category": image_result["likely_category"],
        "features": features
    }

    return result


if __name__ == "__main__":
    output = run_pipeline("sample_audio.wav", "sample_image.jpg")
    print(output)
