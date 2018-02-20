from app import db
from datetime import datetime

# migrating works as follows:

# Each time a change is made to the database structure, a migration document is created which says
# what the change is, and this is stored in a special migration directory.
# They all just stay there without changing the database for now.
# You have to explicitly tell it to make the migrations, and then it will go through all the 
# migration documents and run them (chronologically).

# The changes include:
# - You have defined a new model which has no database yet - in this case the database will be created from scratch
# - You have changed an exisiting model - in this case the database structure will be changed to match the model.

# > flask db-... (come from Flask-Migrate)
# > flask db init (creates the special migration directory)
# > flask db migrate (creates a migration script)
# > flask db migrate -m "my comment" (allows you to add a comment to the migration script)
# > flask db ugrade (carries out the migrations)

############################################################################
# IMPORTANT: The class name for each model must start with a CAPITAL letter (e.g. User)
# the database table will have the same name, but starting with a LOWERCASE letter (e.g. user)
############################################################################

############################################################################
# Creating a relationship between two different models / database tables:
############################################################################
# 1-to-1 relationship: can define it either way round
# 1-to-many or many-to-1 relationship (e.g. 1 user to many posts)
# - on the "1" side (e.g. 1 user), use db.relationship to add a relationship
# - on the "many" side (e.g. many posts), use db.ForeignKey

class User(db.Model):
    id            = db.Column(db.Integer,     primary_key=True)
    username      = db.Column(db.String(64),  index=True, unique=True)
    email         = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # this is not a real extra field, just a link
    # e.g. user_jane.posts will now return all the posts linked to the user user_jane
    # The first argument tells you which model / database table it links to
    # The second argument tells you how to refer back to the user from the post
    # The 'lazy' argument tells you how the database query will be issued.
    # To access/setup the posts from the user: my_user.posts (indicated by the use of the fieldname 'posts')
    # To access/setup the user from the posts: my_post.author (indicated by backref)

    def __repr__(self):
        return '<User {}>'.format(self.username)   
        
# User inherits the class "db.Model" (from Flask-SQLAlchemy).
# This class has class variables (called fields) such as:
# - a class called db.Column class, with arguments such as field type / uniqueness / indexed which helps with database searches

# The __repr__ method tells Python how to print objects of this class (useful for debugging).
# Essentially if you create an instance of User and then try and print it, you'll get <User JaneG>

class Post(db.Model):
    id        = db.Column(db.Integer, primary_key=True )
    body      = db.Column(db.String(140) )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow )
    # default timestamp is to use the function utcnow [not the result of the function utcnow()]
    # UTC timestamps will be converted to the user's local time when they are displayed.
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id') )

    def __repr__(self):
        return '<Post {}>'.format(self.body)
        
    # define a new Post by setting body=... and author=... (id is automatic and timestamp is optional)
        
        
        
        
        
        
        
        
        
        
        
        