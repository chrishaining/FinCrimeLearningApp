from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

########################
## Glossary term form ##
########################
class GlossaryTermForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    description = TextAreaField('Description')
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit')


#####################################
## form to update a recommendation ##
#####################################
# class RecommendationForm(FlaskForm):
#     title = StringField('Title', validators = [DataRequired()])
#     text = TextAreaField('Text')
#     # I would like to add a dropdown menu for the section, but it's not part of MVP
#     submit = SubmitField('Submit')


########################
## Search form ##
########################
class SearchForm(FlaskForm):
    # choices = [('Artist', 'Artist'),
    #            ('Album', 'Album'),
    #            ('Publisher', 'Publisher')]
    # select = SelectField('Search for music:', choices=choices)
    search = StringField('')
