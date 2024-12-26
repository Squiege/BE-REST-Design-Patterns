from models import Employee, db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeService:
    @staticmethod
    def get_all_employees():
        return Employee.query.all()

    @staticmethod
    def create_employee(data):
        new_employee = Employee(name=data['name'], position=data['position'])
        db.session.add(new_employee)
        db.session.commit()
        return new_employee
