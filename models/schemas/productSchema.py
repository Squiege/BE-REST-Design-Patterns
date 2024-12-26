from marshmallow import fields
from schema import ma  # Assuming 'ma' is your Marshmallow instance

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_id', 'product_id', 'quantity', 'total_price', 'customer', 'product')

    id = fields.Integer(required=False)  # To avoid receiving 'id' in the payload
    name = fields.String(required=True)
    price = fields.Float(required=True)

# Instantiate single and multiple schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)