from marshmallow import fields
from schema import ma  # Assuming 'ma' is your Marshmallow instance

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_id', 'product_id', 'quantity', 'total_price', 'customer', 'product')

    id = fields.Integer(required=False)  # To avoid receiving 'id' in the payload
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_price = fields.Float(required=True)

    # You can include the related fields if needed
    customer = fields.Nested('CustomerSchema', only=['id', 'name'])
    product = fields.Nested('ProductSchema', only=['id', 'name', 'price'])

# Instantiate single and multiple schemas
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)