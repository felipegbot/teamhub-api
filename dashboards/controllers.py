from flask import request, jsonify
import uuid

from .. import db
from .models import Dashboard

def list_all_dashboards_controller():
    dashboards = Dashboard.query.all()
    response = []
    for dashboard in dashboards: response.append(dashboard.toDict())
    return jsonify(response)

def create_dashboard_controller():
    request_form = request.get_json()

    id = str(uuid.uuid4())
    new_dashboard = Dashboard(
                    id           = id,
                    name         = request_form['name'],
                    user_id = request_form['user_id'],
                    )
    db.session.add(new_dashboard)
    db.session.commit()

    response = Dashboard.query.get(id).toDict()
    return jsonify(response)

def retrieve_dashboard_controller(dashboard_id):
    response = Dashboard.query.get(dashboard_id).toDict()
    return jsonify(response)

def delete_dashboard_controller(dashboard_id):
    Dashboard.query.filter_by(id=dashboard_id).delete()
    db.session.commit()

    return ('Dashboard with Id "{}" deleted successfully!').format(dashboard_id)

def get_dashboard_by_user_id_controller(user_id):
    dashboard = Dashboard.query.filter_by(user_id=user_id).all()
    response = []
    if dashboard is None:
        return jsonify({"error": "No dashboard found for this user_id"}), 404
    else:
        for dash in dashboard: response.append(dash.toDict())
        return jsonify(response)
    
def change_dashboard_controller(dashboard_id):
    request_form = request.get_json()
    dashboard = Dashboard.query.get(dashboard_id)
    dashboard.name = request_form['name']
    db.session.commit()
    response = dashboard.toDict()
    return jsonify(response)
