from app import app
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
    
# This decorator indicates links the function to the shell context
# so that when you run flask shell, this function is called.
# The function itself will register these items in the shell session.
# It is in the form of a dictionary because you can then use these dictionary labels
# within the shell to reference the items.