import os
# basedir is going to be the main directory of the application:
# __file__ is the pathname of the file from which this module was loaded, namely __init__.py
# So .dirname returns the directory name that __init__.py is in.
basedir = os.path.abspath(os.path.dirname(__file__))

# Create a class called Config where we are going to store all our configuration variables
# Note that this is particularly useful as it means we can create instances of this class 
#   if we want to produce a different set of configuration variables.

class Config(object):
    # For each configuration item, ideally it wants to use an environment variable because
    # then it can be changed when you run it. But also provide it with a hardcoded string
    # in case there isn't an environment variable.
    
    # SECRET_KEY: This is used for encrypting usernames etc
    # The 'or' means first look for environment variable, but if not then use 'secret'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    
    # SQLALCHEMY_DATABASE_URI: this is providing the location of the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # There is the option to signal the application every time a change is about to be
    # made in the database - we can turn this off
    SQLALCHEMY_TRACK_MODIFICATIONS = False