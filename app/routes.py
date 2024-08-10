from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify
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
            'body': 'Beautiful day in Chicago!'
        },
        {
            'author': {'username': 'Ethan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# items = [{'id': i, 'item': f"Item {i}"} for i in range(1, 101)]

# @app.route('/items', methods=['GET'])
# def get_items():
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 10))
#     if per_page > 50:
#         return jsonify({"error": "You can see up to 50 items per page"}), 400
#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated_items = items[start:end]
#     return jsonify(paginated_items)