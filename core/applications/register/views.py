# -*- conding: utf-8 -*-

"""
    application app food
    by reosoft mexico
"""

import pprint
from flask import Blueprint, render_template, abort, session, jsonify, request
from functools import update_wrapper
from datetime import timedelta
from flask import make_response, request, current_app

app = Blueprint('register_views', __name__)

@app.route('/ajax/create/step1/', methods=['POST','OPTIONS'])
def step1():

    print request.data

    response = {
        'response': 200
    }
    
    return jsonify(response)