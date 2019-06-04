from config import db


class RestFull_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), default="")
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    products = db.relationship("Product", backref="user", lazy='dynamic')


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)


class TempModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(120))
    tempDemo = db.Column(db.String(120))


class shubhamModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(120))
    shubhamDemo = db.Column(db.String(120))


class floatData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Float, default=0.0)
