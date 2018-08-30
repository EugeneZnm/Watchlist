from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

# instantiate manager class
manager = Manager(app)
# new command to launch application server
manager.add_command('server', Server)
if __name__ == '__main__':
    manager.run()
