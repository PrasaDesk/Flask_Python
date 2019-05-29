from config import app, db
from user.view import register, getUsers, getOne, updateUser, deleteUser
from flask_restful import Resource, Api
from product.view import AddProduct, GetAllProducts

api = Api(app)


api.add_resource(register, '/')
api.add_resource(getUsers, '/')
api.add_resource(getOne, '/<string:id>')
api.add_resource(updateUser, '/<string:id>')
api.add_resource(deleteUser, '/<string:id>')

api.add_resource(AddProduct, '/product')
api.add_resource(GetAllProducts, '/product')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=6000)