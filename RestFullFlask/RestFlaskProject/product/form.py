from config import ma
from .model import Product


class ProductForm(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'user_id')


product_schema = ProductForm()
products_schema = ProductForm(many=True)