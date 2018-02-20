# import flask (it will need to be installed using pip install inside venv)
from flask import Flask
# import the Config class that I created in config.py
from config import Config
# import some more packages (these need to be installed using pip install inside venv)
from flask_sqlalchemy import SQLAlchemy # (for using a database)
from flask_migrate import Migrate # (for migrating data if the database structure changes)

app = Flask(__name__)
app.config.from_object(Config)
# The configuration variables will be set up as a python dictionary
# They can be accessed by using: app.config['SECRET_KEY'], eg:
print "secret key = "+ app.config['SECRET_KEY']

# set up the database:
db = SQLAlchemy(app)
# set up the option to migrate the database (i.e. migrate the data if the database structure changes)
migrate = Migrate(app,db)

# import routes.py and models.py which are two files that you have to create yourself
from app import routes, models
