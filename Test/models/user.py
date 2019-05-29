from config import db

class Demo_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), default="")
    first_name = db.Column(db.String(15), default="")
    last_name = db.Column(db.String(15), default="")
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))