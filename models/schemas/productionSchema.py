from marshmallow import fields
from schema import ma  # Assuming 'ma' is your Marshmallow instance

class ProductionSchema(ma.Schema):
    class Meta:
        fields = ( 'id', 'product_id', 'quantity_produced', 'date_produced', 'product')

    id = fields.Integer(required=False)  # To avoid receiving 'id' in the payload
    product_id = fields.db.relationship("product_id", back_populates="product_schemas")
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)
    product = fields.Nested('ProductSchema', only=['id', 'name', 'price'])

# Instantiate single and multiple schemas
production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)