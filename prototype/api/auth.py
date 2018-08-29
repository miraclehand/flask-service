import functools
import jwt
import datetime
from prototype import app, db
from prototype.models import User
from flask_restful import Resource
from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

def token_required(f):
	@functools.wraps(f)
	def decorated(*args, **kwargs):
		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return jsonify({'message' : 'Token is missing'}), 401
			#return redirect(url_for('auth.login'))

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = User.query.filter(User.username == data['username']).first()
		except:
			return jsonify({'message' : 'Token is invalid'}), 401
		return f(current_user, *args, **kwargs)
	return decorated

class Login(Resource):
	def __init__(self):
		super(Login, self).__init__()

	def get(self):
		auth = request.authorization
		#token = request.headers.get("Authorization", None)

		if not auth:
			return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required!'"})

		user = User.query.filter(User.username == auth.username).first()
		if not user:
			return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required!'"})

		if check_password_hash(user.password, auth.password):
			token = jwt.encode({'public_id' : user.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

			return jsonify({"token" : token.decode("UTF-8")})

		return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required!'"})

class Join(Resource):
	def __init__(self):
		super(Join, self).__init__()

	def get(self):
		print('get')

		users = User.query.all()
		output = []
		for user in users:
			print("user", user.username)
			user_data = {}
			user_data['username'] = user.username
			user_data['password'] = user.password
			output.append(user_data)

		return jsonify({"users" : output})

	#update-task
	def put(self):
		data = request.get_json()

		username = data["username"]
		password = data["password"]
		new_password = data["new_password"]

		user = User.query.filter(User.username == username).first()

		if user:
			return make_response("Exists username", 401, {"WWW-Join" : "Exists username"})
		else:
			if check_password_hash(user.password, password):
				hashed_password = generate_password_hash(new_password, method='sha256')
				new_user = User(username=username,password=hashed_password)
				new_user.save()
			else:
				return make_response("Not matched password", 401, {"WWW-Join" : "Not matched password"})

		return {'task':'login put', 'id':username, 'pw':password}, 201

	#add-task
	def post(self):
		data = request.get_json()

		username = data["username"]
		password = data["password"]

		user = User.query.filter(User.username == username).first()

		if user:
			return make_response("Exists username", 401, {"WWW-Join" : "Exists username"})
		else:
			hashed_password = generate_password_hash(password, method='sha256')
			new_user = User(username=username,password=hashed_password)
			new_user.save()

		return {'task':'login post', 'id':username, 'pw':password}, 201

	#delete-task
	def delete(self):
		data = request.get_json()

		username = data["username"]
		password = data["password"]

		user = User.query.filter(User.username == username).first()

		if user:
			if check_password_hash(user.password, password):
				user.remove()
			else:
				return make_response("Not matched password", 401, {"WWW-Join" : "Not matched password"})
		else:
			return make_response("Exists username", 401, {"WWW-Join" : "Exists username"})

		return {'task':'login delete', 'id':username, 'pw':password}, 201

