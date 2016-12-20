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

#CROSSDOMAIN - DECORADOR HTML
def crossdomain(origin=None, methods=None, headers=None,max_age=21600, attach_to_all=True,automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()
 
    def get_methods():
        if methods is not None:
            return methods
 
        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']
 
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp
 
            h = resp.headers
 
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp
 
        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/ajax/create/step1/', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def step1():

    response = {}
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
    
    check_user = r.db('food').table('user_register').filter({'email': users['email']}).run(conn)
    check_user = list(check_user)
    if len(check_user) > 0:
        
        response['success'] = 200
        response['message'] = u'El usuario ya existe'
        response['code'] = 1

    else:    
     
        insert = r.db(current_app.config['DATABASE']).table('user_register').insert(users).run(conn)
        response['success'] = 200
        response['message'] = u'Usuario registrado'
        response['code'] = 0

    pprint.pprint(response)
    return jsonify(response)