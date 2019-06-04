from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/checkDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Email(db.Model):
    """
        This is EmailTemplates model which store a sample email templates in database
            - If status is False then that user is consider as Deleted or deactive
    """
    __tablename__ = "email"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), default="")
    subject = db.Column(db.String(50), default="")
    containt = db.Column(db.String(250), default="")
    isForAll = db.Column(db.Boolean,  default=False)
    status = db.Column(db.Boolean, default=False)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
