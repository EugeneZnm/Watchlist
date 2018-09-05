# import create_app function and dbinstance from app/__init__
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Server

#

# Creating app instance
app = create_app('development')


# instantiate manager class
manager = Manager(app)
# new command to launch application server
manager.add_command('server', Server)
# Initialise Migrate class in app instance
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# manager shell decorator to create a shell context
@manager.shell
def make_shell_context():
    """
    make_shell_context function allowing passing of properties into our shell
    pass Role class in shell context
    :return: returning app and database instance with the User class
    """
    return dict(app=app, db=db, User=User, Role=Role)


if __name__ == '__main__':
    manager.run()
