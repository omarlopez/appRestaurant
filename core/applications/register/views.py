# -*- conding: utf-8 -*-

"""
    application app food
    by reosoft mexico
"""

import pprint
from flask import Blueprint, render_template, abort, session, jsonify, request

app = Blueprint('register_views', __name__)

@app.route('/ajax/create/step1/', methods=['POST'])
def step1():

    response = {}
    
    print request.__dict__

    return jsonify(response)