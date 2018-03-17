import os
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASKY_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def run():
    app.run()


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
un()
