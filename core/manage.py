# -*- conding: utf-8 -*-

"""
    application app food
    by reosoftmexico
"""

from main import app
from flask.ext.script import Manager

manager = Manager(app)


## database app_food

@manager.command
def create_db():

	conn = r.connect(host=current_app.config['RETHINKDB_HOST'])

	r.db_create(current_app.config['DATABASE']).run(conn)
	print '--> success database app food'

	r.db(current_app.config['DATABASE']).table_create('user_register').run(conn)
	print '--> success user user_register'

	r.db(current_app.config['DATABASE']).table_create('platillo_comida').run(conn)
	print '--> success platillo de comida'


if __name__=='__main__':
    manager.run()