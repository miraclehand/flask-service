import os
from flask import Flask


def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)

	if test_config is None:
		#app.config.from_pyfile('config.py', silent=True)
		app.config.from_mapping(
			SECRET_KEY='dev',
			DATABASE=os.path.join(app.instance_path, 'prototype.sqlite') ,
		)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import db
	db.init_app(app)

	from . import auth
	app.register_blueprint(auth.bp)

	from . import blog
	app.register_blueprint(blog.bp)	
	app.add_url_rule('/', endpoint = 'index')

	return app
