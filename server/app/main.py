from flask import Flask, request
from flask import redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "Hello, world!"


@app.route("/user/<username>")
def show_user(username: str) -> str:
    return f"User {username}"


@app.route("/post", methods=["POST"])
def post_content() -> dict:
    content = request.get_json()
    print(content)
    print(type(content))
    return content


app.config.update(dict(
    SECRET_KEY="powerful secret key",
    WTF_CSRF_SECRET_KEY="a csrf secret key"))


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    photo = FileField()


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        print(form.name.data)
        return "form submitted"
    return render_template('submit.html', form=form)
