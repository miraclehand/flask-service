import os
from flask_restful import Api

from prototype import views
from prototype.db import db
from prototype.app import app
from prototype.api import auth
from prototype.api import prod 

views.AuthView.register(app)
views.View.register(app)

api = Api(app)

# resource map
api.add_resource(auth.Login, '/api/v1.0/auth/login', endpoint='login')
api.add_resource(auth.Join, '/api/v1.0/auth/join', endpoint='join')
api.add_resource(prod.ProductAPI, '/api/v1.0/prod/product','/api/v1.0/prod/product/<product_id>', endpoint='product')
api.add_resource(prod.SupplierAPI, '/api/v1.0/prod/supplier', '/api/v1.0/prod/supplier/<supplier_id>', endpoint='supplier')

def create_app(test_config=None):
	if test_config is None:
		#app.config.from_pyfile('config.py', silent=True)
		app.config.from_mapping(
			SECRET_KEY='dev',
			#DATABASE=os.path.join(app.instance_path, 'prototype.sqlite') ,
		)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	#from . import db
	#db.init_app(app)
	#db.set_db(db)

	#from . import home
	#app.register_blueprint(home.bp)	

	#from . import auth
	#app.register_blueprint(auth.bp)

	#from . import blog
	#app.register_blueprint(blog.bp)	

	#app.add_url_rule('/', endpoint = 'index')

	# resource map
	#api.add_resource(home.CHome, '/<string:todo_id>')

	#api.add_resource(home.CHome, '/<string:todo_id>')
	#api.add_resource(home.TodoList, '/todos')
	#api.add_resource(home.Todo, '/todos/<todo_id>')

	#api.add_resource(auth.CLogin, '/auth/login')
	#api.add_resource(auth.CRegister, '/auth/register')
	#api.add_resource(blog, '/blog')
	#app.register_blueprint(auth.bp)
	return app

