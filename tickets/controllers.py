from flask import request, jsonify
import uuid

from .. import db
from .models import Ticket

def list_all_tickets_controller():
    tickets = Ticket.query.all()
    response = []
    for ticket in tickets: response.append(ticket.toDict())
    return jsonify(response)

def create_ticket_controller():
    request_form = request.get_json()

    id = str(uuid.uuid4())
    new_ticket = Ticket(
        id           = id,
        name         = request_form['name'],
        description = request_form['description'],
        status = request_form['status'],
        dashboard_id = request_form['dashboard_id'],
        priority = request_form['priority']
    )
    db.session.add(new_ticket)
    db.session.commit()

    response = Ticket.query.get(id).toDict()
    return jsonify(response)

def retrieve_ticket_controller(ticket_id):
    response = Ticket.query.get(ticket_id).toDict()
    return jsonify(response)

def delete_ticket_controller(ticket_id):
    Ticket.query.filter_by(id=ticket_id).delete()
    db.session.commit()

    return ('Ticket with Id "{}" deleted successfully!').format(ticket_id)

def update_ticket_status_controller(ticket_id):
    request_form = request.get_json()
    ticket = Ticket.query.get(ticket_id)
    ticket.status = request_form['status']
    db.session.commit()

    response = Ticket.query.get(ticket_id).toDict()
    return jsonify(response)

def update_ticket_data_controller(ticket_id):
    request_form = request.get_json()
    ticket = Ticket.query.get(ticket_id)
    ticket.name = request_form['name']
    ticket.description = request_form['description']
    ticket.priority = request_form['priority']
    db.session.commit()

    response = Ticket.query.get(ticket_id).toDict()
    return jsonify(response)


def get_tickets_by_dashboard_controller(dashboard_id):
    tickets = Ticket.query.filter_by(dashboard_id=dashboard_id).all()
    response = []
    for ticket in tickets: response.append(ticket.toDict())
    return jsonify(response)