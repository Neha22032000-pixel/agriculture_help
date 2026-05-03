# main.py

from speech_to_text import transcribe_audio
from image_analysis import analyze_image
from triage_logic import compute_severity
from utils import parse_transcription


def generate_explanation(severity, category):
    if severity == "🟢 Safe":
        return f"This looks like a mild {category} condition. It is not urgent. Maintain hygiene and monitor for a few days."
    elif severity == "🟡 Monitor":
        return f"This may be a {category} condition. Monitor closely and consider visiting a pharmacist if it does not improve."
    else:
        return f"This may be a serious {category} condition. Please consult a doctor as soon as possible."


def run_pipeline(audio_path, image_path):
    print("🔹 Step 1: Transcribing audio...")
    text = transcribe_audio(audio_path)
    print("Transcription:", text)

    print("\n🔹 Step 2: Extracting structured features...")
    features = parse_transcription(text)
    print("Features:", features)

    print("\n🔹 Step 3: Analyzing image...")
    image_result = analyze_image(image_path)
    print("Image Result:", image_result)

    print("\n🔹 Step 4: Computing severity...")
    severity = compute_severity(features, image_result["confidence"])
    print("Severity:", severity)

    print("\n🔹 Step 5: Generating explanation...")
    explanation = generate_explanation(severity, image_result["likely_category"])

    result = {
        "transcription": text,
        "features": features,
        "image_analysis": image_result,
        "severity": severity,
        "explanation": explanation
    }

    return result


if __name__ == "__main__":
    # Replace with your actual file paths
    audio_path = "sample_audio.wav"
    image_path = "sample_image.jpg"

    output = run_pipeline(audio_path, image_path)

    print("\n✅ FINAL OUTPUT")
    for key, value in output.items():
        print(f"{key}: {value}")
