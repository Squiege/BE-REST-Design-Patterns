from sqlalchemy.orm import Session
from database import db
from models.customer import Customer

def save_customer_data(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(
                name=customer_data['name'], 
                email=customer_data['email'], 
                phone=customer_data['phone']
            )
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
        return {
            "id": new_customer.id,
            "name": new_customer.name,
            "email": new_customer.email,
            "phone": new_customer.phone
        }

def get_customer_by_id(customer_id):
    with Session(db.engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            return {"error": "Customer not found"}
        return {
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone
        }

def get_all_customers():
    with Session(db.engine) as session:
        customers = session.query(Customer).all()
        return [
            {
                "id": cust.id,
                "name": cust.name,
                "email": cust.email,
                "phone": cust.phone
            }
            for cust in customers
        ]
