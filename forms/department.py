from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField("Department name", validators=[DataRequired()])
    email_dep = EmailField("Department email", validators=[DataRequired()])
    members = StringField("Members' id")
    submit = SubmitField('Continue')