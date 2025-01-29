from flask import Flask, render_template, request, flash, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "muhammedyaseen2417@gmail.com"
EMAIL_PASSWORD = "yqinqurelaydbyab"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    full_message = f"From: {name} <{email}>\n\n{message}"
    msg = MIMEText(full_message)
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(email, EMAIL_ADDRESS, msg.as_string())

        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Error sending message: {str(e)}", "danger")

    return redirect("/contact")

if __name__ == "__main__":
    app.run(debug=True)
