from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = "Home")

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested from user {form.username.data}")
        return redirect(url_for('index'))
    return render_template("login.html", title = "Sign In", form = form)
