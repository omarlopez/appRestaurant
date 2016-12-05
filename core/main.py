# -*- conding: utf-8 -*-

"""
    application app food
    by omarlaszloo@gmail.com
"""

from flask import Flask, redirect, session
from flask_appconfig.env import from_envvars

app = Flask('coreadmin')
from_envvars(app.config, prefix='FLASK_')

from applications.register.views import app as register_views
app.register_blueprint(register_views)