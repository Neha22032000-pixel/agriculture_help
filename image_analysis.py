def parse_transcription(text):
    text = text.lower()

    def has(words):
        return any(w in text for w in words)

    return {
        "itching": has(["itch", "khujli"]),
        "pain": has(["pain", "dard"]),
        "spread": has(["spread", "fail", "bad raha"]),
        "duration": extract_days(text),
        "pus": has(["pus", "peep"]),
        "worsening": has(["worse", "zyada", "bad raha"]),
        "fever": has(["fever", "bukhar"])
    }
