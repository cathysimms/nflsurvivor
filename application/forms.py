from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class HomeForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Enter Username')
