from flask import request
from ..app import app
from .controllers import list_all_dashboards_controller, create_dashboard_controller, retrieve_dashboard_controller, delete_dashboard_controller, get_dashboard_by_user_id_controller, change_dashboard_controller

@app.route("/dashboards", methods=['GET'])
@app.login_manager.user_loader
def list_dashboards():
    if request.method == 'GET': return list_all_dashboards_controller()
    else: return 'Method is Not Allowed'

@app.route("/dashboards/create", methods=['POST'])
@app.login_manager.user_loader
def create_dashboard():
    if request.method == 'POST': return create_dashboard_controller()
    else: return 'Method is Not Allowed'

@app.route("/dashboards/getDashboardById/<id>", methods=['GET'])
@app.login_manager.user_loader
def get_dashboard_by_id(id):
    if request.method == 'GET': return retrieve_dashboard_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/dashboards/changeDashboardName/<id>", methods=['PUT'])
@app.login_manager.user_loader
def change_dashboard_name(id):
    if request.method == 'PUT': return change_dashboard_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/dashboards/delete/<id>", methods=['DELETE'])
@app.login_manager.user_loader
def delete_dashboard_by_id(id):
    if request.method == 'DELETE': return delete_dashboard_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/dashboards/getDashboardByUserId/<user_id>", methods=['GET'])
@app.login_manager.user_loader
def get_dashboard_by_user_id(user_id):
    if request.method == 'GET': return get_dashboard_by_user_id_controller(user_id)
    else: return 'Method is Not Allowed'
