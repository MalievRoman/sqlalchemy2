from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, SubmitField, DateTimeField, SelectMultipleField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField('Job title', validators=[DataRequired()])
    w_size = IntegerField('Work size (hours)', validators=[DataRequired()])
    collab = StringField("Collaborators' id")
    start = DateTimeField("Start date", format='%Y-%m-%d %H:%M:%S', default=datetime.now())
    hazard_category = SelectMultipleField('Hazard level', choices=['0', '1', '2', '3', '4', '5', '6', '7'])
    end = DateTimeField("End date", format='%Y-%m-%d %H:%M:%S', default=datetime.now())
    finish = BooleanField("Did you do that?")

    submit = SubmitField('Continue')