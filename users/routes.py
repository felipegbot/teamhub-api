from flask import request
from flask_login import login_required
from ..app import app
from .controllers import list_all_users_controller, create_user_controller, retrieve_user_controller, delete_user_controller, login_user_controller, logout_user_controller, change_user_controller

@app.route('/login', methods=['POST'])
def login():
    return login_user_controller()

@app.route('/logout', methods=['POST'])
@app.login_manager.user_loader
def logout():
    return logout_user_controller()

@app.route("/users/create", methods=['POST'])
def create_user():
    return create_user_controller()

@app.route("/users/getUsers", methods=['GET'])
@app.login_manager.user_loader
def get_users():
    return list_all_users_controller()

@app.route("/users/getUserById/<id>", methods=['GET'])
@app.login_manager.user_loader
def get_user_by_id(id):
    if request.method == 'GET': return retrieve_user_controller(id)
    else: return 'Method is Not Allowed'


@app.route("/users/delete/<id>", methods=['DELETE'])
@app.login_manager.user_loader
def retrieve_update_destroy_user(id):
    if request.method == 'DELETE': return delete_user_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/users/changeUser/<id>", methods=['PUT'])
@app.login_manager.user_loader
def change_user_by_id(id):
    if request.method == 'PUT': return change_user_controller(id)
    else: return 'Method is Not Allowed'
