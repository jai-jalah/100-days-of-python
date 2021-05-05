from flask import Flask, render_template, request
import requests
import smtplib
from decouple import config

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()
EMAIL = config("EMAIL")
EMAIL_PASS = config("EMAIL_PASS")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, EMAIL_PASS)
        connection.sendmail(EMAIL, EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)