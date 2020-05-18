from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
# import flask.ext

app = Flask(__name__)

app.config['SECRET_KEY']= 'secretkey'

######################
### Database setup ###
######################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# import flask_whooshalchemy as wa
# configure whoosh
# app.config['WHOOSH_BASE'] = 'whoosh'

# create an index for whoosh. I'm not sure where this should go - models.py? Or can I just put it here and import the models here?
# from project.models import Section, Recommendation, GlossaryTerm
# wa.whoosh_index(app, Section, Recommendation, GlossaryTerm)

db = SQLAlchemy(app)
Migrate(app,db)

from project import routes
