# 🎅 Secret Santa Video Emailer

A Python-based Secret Santa organizer that adds an **AI-powered twist** —  
each participant receives a *pre-generated SoraAI video* of the person they’re buying a gift for, delivered secretly via email.

---

## ✨ Features
- 🎁 Randomized derangement algorithm ensures no self-assignments.
- 📧 Automatic email delivery with personalized AI video attachments.
- ⏳ Suspense mode — send one email at a time with a button press for added tension.
- 🔒 Gmail App Password authentication for secure email sending.
- 🧠 Modular and easy-to-use code structure.

---

## 🛠️ How It Works
1. Add participants (name, email, and video path).
2. The script randomizes who each person gets (no repeats or self-pairings).
3. One click per person — the email (with video) is sent and announced in the console.
4. The mystery unfolds one by one.

---

## 🚀 Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/YOURUSERNAME/secret-santa-ai.git
   cd secret-santa-ai
   
2. Install Requirements:
    ```bash
    pip install -r requirements.txt

3. Edit secret_santa.py with you participant info and Gmail App password.
   
4. Run:
   ```bash
   python secret_santa.py
