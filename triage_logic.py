def compute_severity(features, image_confidence):
    score = 0

    if features.get("pain"): score += 2
    if features.get("spread"): score += 2
    if features.get("duration", 0) > 5: score += 1
    if features.get("pus"): score += 3
    if features.get("worsening"): score += 2

    # confidence-aware boost
    if image_confidence < 0.7:
        score += 2

    # safety override
    if features.get("pus") or features.get("fever") or features.get("severe_pain"):
        return "🔴 Urgent"

    if score <= 2:
        return "🟢 Safe"
    elif score <= 5:
        return "🟡 Monitor"
    else:
        return "🔴 Urgent"
