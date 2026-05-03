def parse_transcription(text):
    """
    Convert raw text into structured features
    VERY basic version (we improve later)
    """
    text = text.lower()

    return {
        "itching": "yes" in text,
        "pain": "pain yes" in text,
        "spread": "spreading yes" in text,
        "duration": extract_days(text),
        "pus": "pus" in text,
        "worsening": "worse" in text
    }


def extract_days(text):
    import re
    match = re.search(r'(\d+)\s*day', text)
    return int(match.group(1)) if match else 3
