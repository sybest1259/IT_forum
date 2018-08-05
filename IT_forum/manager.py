from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app

manager = Manager(create_app('default'))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()