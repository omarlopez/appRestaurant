# -*- conding: utf-8 -*-

"""
    application app food
    by reosoft mexico
"""
import rethinkdb as r
import pprint
import json
from flask import Blueprint, render_template, abort, session, jsonify, request
from functools import update_wrapper
from datetime import timedelta
from flask import make_response, request, current_app

app = Blueprint('register_views', __name__)

@app.route('/ajax/create/step1/', methods=['POST','OPTIONS'])
def step1():

    response = {}
    
    if request.method == 'POST':

        conn = r.connect(host=current_app.config['RETHINKDB_HOST'])

        users = json.loads(request.data)
        users = {
            'name': users['name'],
            'user': users['user'],
            'email': users['email'],
            'password': users['password'],
            'ubication': [],
            'sale': []
        }
        
        insert = r.db(current_app.config['DATABASE']).table('user_register').insert(users).run(conn)
        response['success'] = 200
    
    return jsonify(response)