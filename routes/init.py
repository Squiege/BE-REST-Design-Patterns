from flask import Blueprint, jsonify, request
from services import EmployeeService

bp = Blueprint('main', __name__)

@bp.route('/employees', methods=['GET'])
def get_employees():
    employees = EmployeeService.get_all_employees()
    return jsonify([e.to_dict() for e in employees])  # Assume `to_dict()` is implemented in Employee

@bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee = EmployeeService.create_employee(data)
    return jsonify(employee.to_dict()), 201

def register_routes(app):
    app.register_blueprint(bp)
