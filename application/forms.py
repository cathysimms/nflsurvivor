from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class HomeForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Enter Username')
    #week = SelectField('Week', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11'),(12,'12')])
