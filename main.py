from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def base(prof):
    if "инженер" in prof or "строитель" in prof:
        return render_template("profession.html", profession=1)
    else:
        return render_template("profession.html", profession=0)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
