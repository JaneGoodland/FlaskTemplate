from app import app
from flask import render_template, flash, redirect, url_for
from forms import LoginForm
from app.models import User, Post
# Note that flask will need to be installed using pip install inside venv

# some options for what you can return:
# - a string:   return "my text"
# - a template: return render_template('template_name.html', dynamic_thing='value', other_dynamic_thing='value')
# For the templates, you need to import the module from Flask
# This comes from Jinja2 which is the template engine and is found within Flask

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    print users
    
    user = {'username': 'Jane'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    # return render_template('index.html', title='Home')
    
    
@app.route('/login', methods=['GET', 'POST'])
# the default is methods=['GET']
# If you tried to run this route with just methods=['GET'] then submitting the form
# would generate a "method not allowed" error because it would be trying to do a POST
def login():
    loginform = LoginForm() # create an instance of the LoginForm class
    if loginform.validate_on_submit():
        # This section gets called iff SUCCESSFUL POST
        # i.e. it arrives via submit being pressed
        flash('Login requested for user {}, remember_me={}'.format(loginform.username.data, loginform.remember_me.data))
        # flash allows you to send a message        
        return redirect(url_for('index'))
        # the url_for function (which comes with Flask) works out what the url is for "def index()"
        # You could also just type redirect('/index') - this will work but you might change the url link later so it's not good practice
    else:
        # This section gets called iff GET or UNSUCCESSFUL POST
        # i.e. it arrives at via being directed to this url (GET)
        # or it arrives because someone left a field empty in the login form (for example)
        return render_template('login.html', title='Login', form=loginform)
    
        
# TODO got to here: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
# I have just pip-installed the first 2 things and then stopped        