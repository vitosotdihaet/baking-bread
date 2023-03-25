from app import db, app
from flask import abort, jsonify, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

from models import User


@app.route('/login')
def login():
    return 'Login'

@app.route('/logout')
def logout():
    return 'Logout'

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None: # check for missing arguments
        abort(400)

    user = User(username=username)
    user.hash_password(password)

    try: # check if user already exists
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    return "something in return"

@app.route('/', methods=['GET'])
def test():
    return jsonify({'hello': 'hello'})
