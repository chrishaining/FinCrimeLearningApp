from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

###
class GlossaryTermForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    description = TextAreaField('Description')
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit the new term')
