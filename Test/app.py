from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
from .api.xyz import hello
from .api.register_user import home, register
from .config import db, app

from .config import app, db
from .forms.user_form import registerForm
from .models.user import Demo_User

from werkzeug.security import generate_password_hash, check_password_hash


#app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def home_call():
    return home()

@app.route('/register', methods=['POST'])
def regi():
    return register()

if __name__ == '__main__':

    db.create_all()
    app.run(debug=True, port=2000)

