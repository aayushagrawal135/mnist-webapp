from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Aayush"}
    posts = [
        {
            "author": {"username": "Aman"},
            "body": "HP, Anime, Marvel, DC, Pokemon forever"
        },
        {
            "author": {"username": "Skeny"},
            "body": "HP forever"
        }
    ]
    return render_template("index.html", title = "Home", user = user, posts = posts)
