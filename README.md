# 🎅 Secret Santa Video Emailer

A Python-based Secret Santa organizer that adds an **AI-powered twist** —  
each participant can receive a *pre-generated AI video* of the person they’re buying a gift for, delivered secretly via email.
Don't want to attach videos? No problem, just uncheck the box!

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
1. Download the HTMl and app.py files, and place them in the same folder.

2. Install the flask dependancies:
   ```bash
   python -m pip install flask

3. Configure your Gmail App Password and add it to the app.py file
   
4. Run the following command in the terminal in the file:
   ```bash
   python app.py
   
5. Go to your browser: 
    ```bash
    http://127.0.0.1:5000/
