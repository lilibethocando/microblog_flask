from app import app
from flask import render_template
from .forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {
        "username" : "Lilibeth"
    }

    posts = [
        {
            'author': {'username': 'Michelle'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Ethan'},
            'body': 'The Avengers movie was so coll!'
        }
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)