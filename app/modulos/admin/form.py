from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  user = StringField('User', validators =[DataRequired()])
  senha = PasswordField('senha', validators =[DataRequired()])