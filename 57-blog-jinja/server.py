from flask import Flask, render_template
import datetime
import requests

curr_year = datetime.datetime.now().year
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", curr_year=curr_year)


@app.route("/guess/<name>")
def convertor(name):
    gender_res = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_res.json()["gender"]
    age_res = requests.get(f"https://api.agify.io?name={name}")
    age = age_res.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)