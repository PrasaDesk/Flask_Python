from config import db
from product.model import Product

class RestFull_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), default="")
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    products = db.relationship("Product", backref="user", lazy='dynamic')