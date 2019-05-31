from config import app, db
from user.view import register, getUsers, getOne, updateUser, deleteUser, userLogin, UserLogoutAccess, TokenRefresh
from flask_restful import Resource, Api
from product.view import AddProduct, GetAllProducts

api = Api(app)
app.config['SWAGGER'] = {"title" : "Swagger-UI", "uiversion": 2}

api.add_resource(register, '/user')
api.add_resource(getUsers, '/user')
api.add_resource(getOne, '/user/<string:id>')
api.add_resource(updateUser, '/user/<string:id>')
api.add_resource(deleteUser, '/user/<string:id>')
api.add_resource(userLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout')
api.add_resource(TokenRefresh, '/refresh')

api.add_resource(AddProduct, '/product')
api.add_resource(GetAllProducts, '/product')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)