from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SECRET_KEY']= 'secretkey'

######################
### Database setup ###
######################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from whoosh.analysis import StemmingAnalyzer
import flask_whooshalchemy
# set the location for the whoosh index
app.config['WHOOSH_BASE'] = 'whoosh'
# set the global analyzer, defaults to StemmingAnalyzer.
app.config['WHOOSH_ANALYZER'] = StemmingAnalyzer()


from project import routes
