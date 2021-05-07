from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email
from decouple import config


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

    def validate_password(FlaskForm, password):
        if len(password.data) < 4:
            raise ValidationError("Password must be at least 8 characters long")


app = Flask(__name__)
app.secret_key = config("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if (
        login_form.validate_on_submit()
        and login_form.email.data == "admin@email.com"
        and login_form.password.data == "12345678"
    ):
        return render_template("success.html")
    else:
        return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)