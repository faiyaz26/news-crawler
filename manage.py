# manage.py


import os
import unittest

from flask_script import Manager

from server import app

manager = Manager(app)

@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    pass


@manager.command
def drop_db():
    """Drops the db tables."""
    pass


@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.run()