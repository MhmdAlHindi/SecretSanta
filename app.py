import os
import random
import smtplib
import ssl
import mimetypes
from email.message import EmailMessage
from flask import Flask, request, jsonify, send_from_directory

#Flask Browser
app = Flask(__name__)

#Main email sending function, customize message below
def send_email(sender_email, sender_password, smtp_server, smtp_port,
               giver, receiver, use_video):
    msg = EmailMessage()
    msg["Subject"] = "Your Secret Santa 🎁"
    msg["From"] = sender_email
    msg["To"] = giver["email"]

    if use_video and receiver.get("video_path"):
        body = f"""Hi {giver['name']},

                Ho ho ho! 🎅
                Watch the video to find out who your person is.
                Shhh... don't tell anyone 😉

                –Santa's Workshop
                123 Elf Road, North Pole
                """
        msg.set_content(body)

        video_path = receiver["video_path"]
        ctype, encoding = mimetypes.guess_type(video_path)
        if ctype is None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)

        with open(video_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype=maintype,
                subtype=subtype,
                filename=os.path.basename(video_path),
            )
    else:
        spacer = "\u200B\n" * 60  # invisible characters + newlines
        body = f"""Hi {giver['name']},

                Ho ho ho! 🎅
                You're buying a gift for...
                {spacer}
                {receiver['name']} 🎁
                Shhh... don't tell anyone 😉

                –Santa's Workshop
                123 Elf Road, North Pole
                """
        msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    #HIDE THIS TO MAKE IT ANONYMOUS FOR YOUR TOO
    # print(f"Sent email to {giver['name']} ({giver['email']}) → {receiver['name']}")


@app.route("/")
def index():
    # Serve the HTML file from the same directory
    return send_from_directory(".", "secret_santa.html")


@app.post("/send_emails")
def send_emails_route():
    data = request.get_json(force=True)
    players = data.get("players", [])
    assignment = data.get("assignment", [])
    use_video = bool(data.get("use_video", False))

    if not players or len(players) < 2:
        return jsonify({"error": "Need at least 2 players"}), 400

    if len(assignment) != len(players):
        return jsonify({"error": "Assignment length mismatch"}), 400

    # Configure your sender here
    sender_email = "YOUR_GMAIL_HERE@gmail.com"
    sender_password = "YOUR_APP_PASSWORD_HERE"  #Get this password from your Gmail App Password settings, be safe!
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    sent_count = 0
    for i, j in enumerate(assignment):
        giver = players[i]
        receiver = players[j]
        send_email(
            sender_email,
            sender_password,
            smtp_server,
            smtp_port,
            giver,
            receiver,
            use_video
        )
        sent_count += 1

    return jsonify({"sent_count": sent_count})


if __name__ == "__main__":
    app.run(debug=True)
