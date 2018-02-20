////////////////////////////////////////////////////////////////////
To get started on Flask:
////////////////////////////////////////////////////////////////////

Set up a virtual environment o work inside:
> virtualenv venv (2.7 version of python)
> python -m venv venv

Activate the virtual environment:
> venv\Scripts\activate (windows)
> source venv/bin/activate (linux)
> deactivate

pip install flask
pip install flask_sqlalchemy
pip install flask_migrate
pip install flask_wtf

////////////////////////////////////////////////////////////////////
To set up and run migrations to create/modify a database:
////////////////////////////////////////////////////////////////////

> flask db-... (come from Flask-Migrate)
> flask db init (creates the special migration directory)
> flask db migrate (creates a migration script)
> flask db migrate -m "my comment" (allows you to add a comment to the migration script)
> flask db ugrade (carries out the migrations)
'upgrade' will create the database (locally, in the current directory) if it does not already exist.
Therefore, if you want your database to be online e.g. MySQL and PostgreSQL, you have to create
the database in the database server before running upgrade.
> flask db downgrade - may be useful, if you realise that it didn't upgrade as you expected,
you can downgrade (i.e. "undo") and then delete the migration script

////////////////////////////////////////////////////////////////////
To run the server locally (in python):
////////////////////////////////////////////////////////////////////

I have seen (on radiator) the use of python serve.py and then on chrome go to epiphron:4242
However, the flask tutorial says:
> export FLASK_APP=my_flask_program.py
> flask run
--> running on http://127.0.0.1:5000 
Note: http://127.0.0.1 is the local server address but only works on the same computer that the program is being run on
So if you're on windows, then this should be fine - just open this web page in chrome
If you're doing it on linux via the server, you might get away with the local address, or you could try epiphron:5000,
  but some ports may get blocked going between computer and server, and 5000 seems to be on of them, 
  so best to run chrome on the server by opening a new linux command prompt:
> /opt/google/chrome/chrome

////////////////////////////////////////////////////////////////////
To interact with the app via python shell:
////////////////////////////////////////////////////////////////////

Open python from the top-level directory (i.e. not inside 'app')
Then you can do stuff like:
> from app import db
> from app.models import User, Post
> u = User(username='john', email='john@example.com') <- create a user
we run inside a db session until we commit that session
whilst running inside the db session, we can add whatever rows we like:
> db.session.add(u)   <- add a user 
we can scrap the session:
> db.session.rollback()
And when we are happy with this session, we can commit it:
> db.session.commit() <- at this point, the new rows are added to the database

Or, you can start in the app directory, and then do:
setup imports in my_flask_program.py under the shell_context_processor decorator
> flask shell <- this command pre-imports the application instance


////////////////////////////////////////////////////////////////////
To do database queries:
////////////////////////////////////////////////////////////////////

users = User.query.all()                                    <- get all the users
users = User.query.order_by(User.username.desc()).all()     <- get all the users in an order
u = User.query.get(1)                                       <- get a user based on their id








