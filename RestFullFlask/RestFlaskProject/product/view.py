from config import app, db
from flask_restful import Resource
from flask import jsonify, request
from .model import Product
from .form import product_schema, products_schema, ProductSchema
from user.model import RestFull_User


class AddProduct(Resource):
    def post(self):
        name = request.json['name']
        price = request.json['price']
        user_id = request.json['user_id']

        print("\n\nAdd Product\n\n")
        print(name, price, user_id)

        if name == '' or price == '':
            return "field is Empty", 400

        user = RestFull_User.query.get(user_id)

        if user:
            new_product = Product(name=name,
                                  price=price,
                                  user_id=user.id)
        else:
            return "User not Exist", 400

        db.session.add(new_product)
        db.session.commit()

        return 'new Product added'


class GetAllProducts(Resource):
    def get(self):
        products = Product.query.all()
        result = products_schema.dump(products)

        return jsonify(result.data)


class Product_Create(Resource):
    def post(self):
        data = request.get_json()

        prod = ProductSchema(data)
        print(prod)
        db.session.add(prod)
        db.session.commit()

        return "new product added"
