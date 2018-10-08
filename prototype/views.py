from flask import render_template
from prototype.forms import LoginForm
from flask_classy import FlaskView

class View(FlaskView):
	def index(self):
		return render_template('index.html', endpoint='index')

class HomeView(FlaskView):
	def index(self):
		return render_template('index.html')

class AuthView(FlaskView):
	def index(self):
		return "This is the index"
	def get(self, id):
		return "The ID is " + str(id)

	def account(self):
		return "This is the account page"

	def signon(self):
		print('signon')
		return render_template('auth/register.html', endpoint='register')

	def login(self):
		print('login')
		form = LoginForm()
		return render_template('auth/login.html', form = form, endpoint='login')

	def loginout(self):
		print('logout')
		return render_template('auth/login.html', endpoint='logout')
