from flask import render_template, flash, redirect, request, jsonify
from app import app
from app.forms import LoginForm
import numpy as np
import json

from app.helper import *

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


@app.route('/submitted_image', methods=["GET", "POST"])
def submitted_image():
    if request.method == 'POST':
        print("incoming towards the server...")
        pixel_array = formatRequest(request.json)
        print(np.shape(pixel_array))
        return 'OK', 200
    else:
        message = {"greeting": "Hello"}
        return jsonify(message)
