from flask import Flask
import random

winning_num = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"
    )


@app.route("/<int:guess>")
def guessed_number(guess):
    if guess < winning_num:
        return (
            "<h1 style='color: red'>Too low, keep going!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
        )
    elif guess > winning_num:
        return (
            "<h1 style='color: purple'>Too High, but at least you're soaring :) </h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
        )
    else:
        return (
            "<h1 style='color: green'>Woohoo! You got it!</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
        )


if __name__ == "__main__":
    app.run(debug=True)