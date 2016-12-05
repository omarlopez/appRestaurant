# -*- conding: utf-8 -*-

"""
    application app food
    by reosoftmexico
"""

from main import app
from flask.ext.script import Manager

manager = Manager(app)


if __name__=='__main__':
    manager.run()