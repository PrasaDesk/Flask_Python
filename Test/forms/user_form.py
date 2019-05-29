from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class registerForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    first_name = StringField('first_name', validators=[Length(min=0, max=15)])
    last_name = StringField('last_name', validators=[Length(min=0, max=15)])
    email = StringField('email', validators=[InputRequired(), Length(min=0, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

