from flask import Blueprint
from controllers.productionController import save

production_blueprint = Blueprint('production_BP', __name__)
production_blueprint.route('/', methods=['POST'])(save)