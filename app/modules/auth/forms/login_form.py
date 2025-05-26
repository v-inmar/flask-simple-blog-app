from flask_wtf import FlaskForm
from wtforms import validators, EmailField, PasswordField, BooleanField, SubmitField

class LoginForm(FlaskForm):
    '''
    FlaskForm for login data
    '''
    email = EmailField(label="Email Address", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=8)])
    remember_me = BooleanField('Remember Me', default="checked")
    submit = SubmitField('Submit')
        
