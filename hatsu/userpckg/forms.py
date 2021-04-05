from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length


class Registerform(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()]) 
    password = PasswordField(validators=[DataRequired(), Length(min=2,max=30)])
    confirm_pw = PasswordField(validators=[DataRequired(), EqualTo('password')])

class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2,max=30)])

class Fanform(FlaskForm):
     title = TextAreaField(validators=[DataRequired()])
     content = TextAreaField(validators=[DataRequired(), Length(min=5, max=2500)])

    
