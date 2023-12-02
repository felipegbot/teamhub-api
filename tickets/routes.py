from flask import request
from .models import Ticket
from flask_login import login_required
from ..app import app
from .controllers import list_all_tickets_controller, create_ticket_controller, retrieve_ticket_controller, delete_ticket_controller, update_ticket_status_controller, get_tickets_by_dashboard_controller, update_ticket_data_controller

@app.route("/tickets", methods=['GET'])
@app.login_manager.user_loader
def list_tickets():
    if request.method == 'GET': return list_all_tickets_controller()
    else: return 'Method is Not Allowed'

@app.route("/tickets/create", methods=['POST'])
@app.login_manager.user_loader
def create_ticket():
    if request.method == 'POST': return create_ticket_controller()
    else: return 'Method is Not Allowed'

@app.route("/tickets/getTicketById/<id>", methods=['GET'])
@app.login_manager.user_loader
def get_ticket_by_id(id):
    if request.method == 'GET': return retrieve_ticket_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/tickets/delete/<id>", methods=['DELETE'])
@app.login_manager.user_loader
def delete_ticket_by_id(id):
    if request.method == 'DELETE': return delete_ticket_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/tickets/changeStatus/<id>", methods=['PUT'])
@app.login_manager.user_loader
def update_ticket_status(id):
    if request.method == 'PUT': return update_ticket_status_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/tickets/changeData/<id>", methods=['PUT'])
@app.login_manager.user_loader
def update_ticket_data(id):
    if request.method == 'PUT': return update_ticket_data_controller(id)
    else: return 'Method is Not Allowed'

@app.route("/tickets/getTicketsByDashboard/<dashboard_id>", methods=['GET'])
@app.login_manager.user_loader
def get_tickets_by_dashboard(dashboard_id):
    if request.method == 'GET': return get_tickets_by_dashboard_controller(dashboard_id)
    else: return 'Method is Not Allowed'