from config import ma
from .model import Product
from marshmallow import fields, Schema


class ProductForm(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'user_id')


product_schema = ProductForm()
products_schema = ProductForm(many=True)


class ProductSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    user_id = fields.Int(required=True)
