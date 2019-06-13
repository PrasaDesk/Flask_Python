from config import app, db, mail
from flask_restful import Resource
from flask import jsonify, request, Flask, url_for, send_from_directory, send_file
from .model import Product
from .form import product_schema, products_schema, ProductSchema
from user.model import RestFull_User
import logging
import os
from werkzeug import secure_filename
from flask_mail import Mail, Message


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


# file_handler = logging.FileHandler('server.log')
# app.logger.addHandler(file_handler)
# app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def create_new_folder(local_dir):
#     newpath = local_dir
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
#     return newpath


class UploadImage(Resource):
    def post(self):
        if request.files['image']:
            img = request.files['image']
            img_name = secure_filename(img.filename)
            # create_new_folder(app.config['UPLOAD_FOLDER'])
            saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
            # app.logger.info("saving {}".format(saved_path))
            img.save(saved_path)
            print("\n\n", saved_path, "\n\n")
            return send_from_directory(app.config['UPLOAD_FOLDER'], img_name, as_attachment=True)

        else:
            return "Where is the image?"


class SendMail(Resource):

    def post(self):
        email = request.json['email']

        msg = Message("Send Mail Tutorial!",
                      sender="yoursendingemail@gmail.com",
                      recipients=[email])
        msg.body = "Yo!\nHave you heard the good word of Python???"
        mail.send(msg)

        return "email send"
