from flask import jsonify, request
from services.employeeService import save_employee, get_employee_by_id, get_all_employees

def save():
    employee_data = request.json
    new_employee = save_employee(employee_data)
    return jsonify(new_employee), 201

def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if "error" in employee:
        return jsonify(employee), 404
    return jsonify(employee), 200

def get_employees():
    employees = get_all_employees()
    return jsonify(employees), 200
