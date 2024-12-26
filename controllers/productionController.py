from flask import request, jsonify
from models.schemas.productionSchema import ProductionSchema
from services import productionService
from marshmallow import ValidationError

def save():
    try:
        production_data = ProductionSchema().load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
        
    new_production = productionService.save(production_data)
    return ProductionSchema.dump(new_production), 201