from flask import Blueprint
from controllers.customerController import save_customer, get_customer, get_customers

customer_blueprint = Blueprint('customer_BP', __name__)

customer_blueprint.route('/customer', methods=['POST'])(save_customer)
customer_blueprint.route('/customer/<int:customer_id>', methods=['GET'])(get_customer)
customer_blueprint.route('/customers', methods=['GET'])(get_customers)
