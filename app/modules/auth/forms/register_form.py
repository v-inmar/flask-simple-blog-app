from flask_wtf import FlaskForm
from wtforms import validators, EmailField, PasswordField, StringField, SubmitField
from app.modules.user.models.user_model import UserModel

class RegisterForm(FlaskForm):
    '''
    FlaskForm for user register data
    '''
    firstname = StringField(label="Firstname", validators=[validators.DataRequired(), validators.Length(min=3, max=32)])
    lastname = StringField(label="Lastname", validators=[validators.DataRequired(), validators.Length(min=3, max=32)])
    email = EmailField(label="Email Address", validators=[validators.DataRequired()]) # Length is validated by wtforms
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=8)])
    repeat_password = PasswordField("Repeat Password", validators=[validators.DataRequired(), validators.EqualTo("password")])
    submit = SubmitField('Submit')

    # Note: validate_on_submit will execute any wtform methods that starts with validate_ after it finished validating above
    # This is wtform convention
    def validate_email(self, form_email):
        '''
        Checks if email is already taken. This is part of the validation
        '''
        user = UserModel.query.filter_by(email=form_email.data).first()
        if user:
            raise validators.ValidationError("Email address is already in use.")
        return None