from sqlalchemy.orm import Session
from database import db
from models.employee import Employee

def save_employee(employee_data):
    with Session(db.engine) as session:
        with session.begin():
            new_employee = Employee(
                name=employee_data['name'], 
                position=employee_data['position']
            )
            session.add(new_employee)
            session.commit()

        session.refresh(new_employee)
        return {
            "id": new_employee.id,
            "name": new_employee.name,
            "position": new_employee.position
        }

def get_employee_by_id(employee_id):
    with Session(db.engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            return {"error": "Employee not found"}
        return {"id": employee.id, "name": employee.name, "position": employee.position}

def get_all_employees():
    with Session(db.engine) as session:
        employees = session.query(Employee).all()
        return [
            {"id": emp.id, "name": emp.name, "position": emp.position}
            for emp in employees
        ]
