import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from forum import create_app, db
# from forum.models import Model


app = create_app(os.environ.get('FORUM_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return {
        'app': app,
        'db': db,
        # 'Model': Model TODO: add models
    }
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
