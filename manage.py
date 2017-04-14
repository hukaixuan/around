import os
from app import create_app, db
# from app.models import User, Post, Label
from flask_script import Manager, Server, Shell

print('create app...')
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
print('done')

def make_shell_context():
	return dict(app=app, db=db)

manager.add_command('runserver', Server(use_debugger=True))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()
