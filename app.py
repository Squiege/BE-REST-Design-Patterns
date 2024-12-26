from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db
from schema import ma
from limiter import limiter

from routes.customerBP import customer_blueprint
from routes.employeeBP import employee_blueprint
from routes.productionBP import production_blueprint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)

    return app
    
def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customer')
    app.register_blueprint(employee_blueprint, url_prefix='/employee')
    app.register_blueprint(production_blueprint, url_prefix='/production')

def configure_rate_limit():
    limiter.limit("5 per day")(customer_blueprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)
