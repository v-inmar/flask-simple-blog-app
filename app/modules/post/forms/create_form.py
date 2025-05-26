from flask_wtf import FlaskForm
from wtforms import validators, TextAreaField, StringField, SubmitField

class PostCreateForm(FlaskForm):
    body_length = 10_000
    title = StringField(label="Title", validators=[validators.DataRequired(), validators.Length(min=1, max=128)])
    body = TextAreaField(label=f"Body ({body_length} words only)", validators=[validators.DataRequired(), validators.Length(min=1, max=body_length)])
    submit = SubmitField(label="Submit")