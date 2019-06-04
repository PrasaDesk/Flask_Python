from config import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), default="")
    price = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('rest_full__user.id'))
