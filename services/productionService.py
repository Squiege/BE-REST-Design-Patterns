from sqlalchemy.orm import Session
from database import db
from models.production import Production

def save_production_data(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(
                product_id=production_data['product_id'], 
                quantity_produced=production_data['quantity_produced'], 
                date_produced=production_data['date_produced']
            )
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
        return {
            "id": new_production.id,
            "product_id": new_production.product_id,
            "quantity_produced": new_production.quantity_produced,
            "date_produced": str(new_production.date_produced)
        }

def get_production_by_id(production_id):
    with Session(db.engine) as session:
        production = session.get(Production, production_id)
        if not production:
            return {"error": "Production record not found"}
        return {
            "id": production.id,
            "product_id": production.product_id,
            "quantity_produced": production.quantity_produced,
            "date_produced": str(production.date_produced)
        }

def get_all_productions():
    with Session(db.engine) as session:
        productions = session.query(Production).all()
        return [
            {
                "id": prod.id,
                "product_id": prod.product_id,
                "quantity_produced": prod.quantity_produced,
                "date_produced": str(prod.date_produced)
            }
            for prod in productions
        ]
