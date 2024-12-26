from flask import jsonify, request
from services.customerService import save_customer_data, get_customer_by_id, get_all_customers

def save_customer():
    customer_data = request.json
    new_customer = save_customer_data(customer_data)
    return jsonify(new_customer), 201

def get_customer(customer_id):
    customer = get_customer_by_id(customer_id)
    if "error" in customer:
        return jsonify(customer), 404
    return jsonify(customer), 200

def get_customers():
    customers = get_all_customers()
    return jsonify(customers), 200
