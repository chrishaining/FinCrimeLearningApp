from flask import Flask

app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app.config['SECRET_KEY']= 'secretkey'

######################
### Database setup ###
######################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from project import routes
