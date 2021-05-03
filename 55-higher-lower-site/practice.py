from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "<b>"

    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1> <p>Yoooo</p> <img src="/Users/JaiJk/Pictures/Dao.jpg" />'


@app.route("/bye")
@make_bold
def bye():
    return str(2)


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name} {number}"


if __name__ == "__main__":
    app.run(debug=True)