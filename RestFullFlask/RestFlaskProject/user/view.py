from config import app, db
from werkzeug.security import generate_password_hash
from .model import RestFull_User
from flask_restful import Resource
from flask import jsonify, request
from .form import user_schema, users_schema
import re


class register(Resource):
    def post(self):
        print('jason = ',request.json)
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        # username validation is Empty or not
        if username == '':
            return "ERROR: Empty Data", 400

        # Email validation with RegEx and for duplication
        emailre = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$";

        if email != "":
            if not re.match(emailre, email):
                return "Invalid Mail", 400
            else:
                if RestFull_User.query.filter(RestFull_User.email == email).one_or_none():
                    return "Email Already Exist", 400
        else:
            return "Empty Email", 400

        # Data save in Database And try to use inbuilt exception for unique Constarint

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = RestFull_User(username=username,
                                 email=email,
                                 password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return "new user added",201


class getUsers(Resource):
    def get(self):
        users = RestFull_User.query.all()
        result = users_schema.dump(users)
        return jsonify(result.data)


class getOne(Resource):
    def get(self, id):
        data = RestFull_User.query.get(id)

        if not data:
            return {"Error":"There is No user with User_ID : "+id}

        result = user_schema.dump(data)
        return jsonify(result.data)


class updateUser(Resource):
    def put(self, id):
        user = RestFull_User.query.get(id)
        username = request.json['username']
        email = request.json['email']

        if username == '':
            return "ERROR: Empty Data", 400

        emailre = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$";

        if email != "":
            if not re.match(emailre, email):
                return "Invalid Mail", 400
            else:
                if RestFull_User.query.filter(RestFull_User.email == email).one_or_none():
                    return "Email Already Exist", 400
        else:
            return "Empty Email", 400

        user.email = email
        user.username = username

        db.session.commit()
        return user_schema.jsonify(user)


class deleteUser(Resource):
    def delete(self, id):
        user = RestFull_User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return user_schema.jsonify(user)