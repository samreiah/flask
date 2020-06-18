from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms import validators, ValidationError

class LoginForm(Form):
   customerId  = TextField("Customer Id", [validators.Required("Please enter Customer Id.")])
   password    = PasswordField('Password', [validators.Required("Please enter Password.")])
   submit      = SubmitField('Login')