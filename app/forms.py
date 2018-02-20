from flask_wtf import FlaskForm # Note that the module is lowercase (flask_wtf), and the imported class (FlaskForm) is uppercase
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
# Note that flask_wtf will need to be installed using pip install inside venv

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')