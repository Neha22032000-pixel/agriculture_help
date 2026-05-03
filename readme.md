# 🩺 Voice + Image-Based Offline Skin Triage Assistant

## 🚨 Problem

In rural and low-resource settings, early diagnosis of common skin conditions is often delayed due to:
- Limited access to doctors
- Low health literacy (difficulty describing symptoms in text)
- Overcrowded healthcare systems
- Lack of reliable first-level screening tools

As a result, minor conditions go untreated and serious infections escalate unnecessarily.

---

## 💡 Our Solution

We build a **multimodal triage assistant** that helps frontline health workers and rural users make **fast, safe, and informed decisions** using:

- 🎤 **Voice input** (Hindi/Hinglish-friendly)
- 📸 **Image input** (skin condition photo)
- 🧠 **Hybrid AI + rule-based decision system**

Instead of diagnosing diseases, the system focuses on:

> **"How urgent is this, and what should be done next?"**

---

## ⚙️ How It Works

### 1. Multimodal Input
- User speaks symptoms → converted to text (speech-to-text)
- User uploads an image of the skin condition

---

### 2. Structured Signal Extraction
From voice input, we extract key signals:
- Itching (yes/no)
- Pain (yes/no)
- Duration (days)
- Spread (yes/no)

Additional adaptive signals:
- Pus/discharge
- Worsening condition
- Fever (if needed)

---

### 3. Image Understanding
The image is analyzed to estimate:
- Likely condition category (fungal, bacterial, allergic, etc.)
- Confidence score

---

### 4. Risk-Aware Triage Engine (Core Innovation)

We combine:
- Structured symptoms
- Image confidence
- Medical heuristics

To compute a **severity score**:
- 🟢 Safe (home care)
- 🟡 Monitor (pharmacist / observe)
- 🔴 Urgent (doctor visit required)

### ⚠️ Safety First
- Low model confidence → severity escalates
- High-risk signals (pus, fever, severe pain) → immediate urgent classification

---

### 5. Actionable Output

Instead of vague responses, we provide:
- Severity level
- Likely category
- Clear next steps

Example:
> "This appears to be a mild fungal infection. Not urgent. Apply antifungal cream and monitor for 3–5 days."

---

## 🧠 Key Innovations

- ✅ **Voice-first interface** for low-literacy users  
- ✅ **Multimodal reasoning (image + symptoms)**  
- ✅ **Hybrid AI + rule-based system** (not just a chatbot)  
- ✅ **Confidence-aware decision making** (risk-sensitive)  
- ✅ **Designed for offline / edge environments**

---

## 🛠️ Tech Stack

- Speech-to-text (e.g., Whisper)
- Multimodal model (e.g., Gemma)
- Python-based triage engine
- Notebook-based demo (Kaggle/Colab compatible)

---

## 🌍 Impact

This system can:
- Assist ASHA workers and rural clinics
- Reduce unnecessary hospital visits
- Enable early detection of serious conditions
- Improve healthcare accessibility at the edge

---

## 🚀 Future Work

- Full offline deployment on mobile devices
- Regional language support expansion
- Integration with public health systems
- Dataset-driven model calibration

---

## 📌 Disclaimer

This is a **triage support tool**, not a medical diagnosis system.  
It is designed to assist decision-making, not replace professional medical advice.

---

## 👩‍💻 Demo

Run `main.py` or use the notebook to simulate:
- Voice input → structured signals
- Image input → classification
- Final triage output

---
