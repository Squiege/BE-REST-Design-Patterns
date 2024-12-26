from flask import Blueprint
from controllers.employeeController import save, get_employee, get_employees

employee_blueprint = Blueprint('employee_BP', __name__)

employee_blueprint.route('/employee', methods=['POST'])(save)
employee_blueprint.route('/employee/<int:employee_id>', methods=['GET'])(get_employee)
employee_blueprint.route('/employees', methods=['GET'])(get_employees)
