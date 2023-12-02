from flask import request, jsonify
import uuid
import hashlib
from .. import db
from .models import User
from flask_login import login_user, logout_user

def list_all_users_controller():
    users = User.query.all()
    response = []
    for user in users: response.append(user.toDict())
    return jsonify(response)

def create_user_controller():
    request_form = request.get_json()

    id = str(uuid.uuid4())
    new_user = User(
        id           = id,
        name         = "mock",
        username = request_form['username'],
        email = request_form['email'],
        password = hashlib.sha256(request_form['password'].encode('utf-8')).hexdigest(),
        specialty = "mock",
        working_area = "mock",
    )
    db.session.add(new_user)
    db.session.commit()

    response = User.query.get(id).toDict()
    return jsonify(response)

def retrieve_user_controller(id):
    user = User.query.get(id).toDict()
    return jsonify(user)

def delete_user_controller(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()

    return ('User with Id "{}" deleted successfully!').format(id)

def login_user_controller():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and hashlib.sha256(data['password'].encode('utf-8')).hexdigest() == user.password:
        login_user(user)
        return jsonify(
            {'message': 'User logged in',
             'user': {
                 'id': user.id,
                 'name': user.name,
                 'username': user.username,
                 'email': user.email,
                 'specialty': user.specialty,
                 'working_area': user.working_area
             }
            }
        ), 200
    return jsonify({'message': 'Invalid credentials'}), 401

def logout_user_controller():
    logout_user()
    return jsonify({'message': 'User logged out'}), 200

def change_user_controller(id):
    request_form = request.get_json()
    user = User.query.get(id)
    user.name = request_form['name']
    user.username = request_form['username']
    db.session.commit()
    response = user.toDict()
    return jsonify(response)
