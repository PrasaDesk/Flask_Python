from config import ma
from .model import RestFull_User


class registerForm(ma.Schema):
    class Meta:
        model = RestFull_User
        # Fields to expose
        fields = ('id', 'username', 'email')


user_schema = registerForm()
users_schema = registerForm(many=True)


# ########################################################################################
# from flask_wtf import FlaskForm, Form
# from wtforms import StringField, PasswordField
# from wtforms.validators import InputRequired, Length


# class registerForm(FlaskForm):
#     username = StringField('username', validators=[Length(min=4, max=15)])
#     email = StringField('email', validators=[Length(min=0, max=50)])
#     password = PasswordField('password', validators=[Length(min=8, max=80)])
##########################################################################################
