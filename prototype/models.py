from prototype import db

class User(db.Document):
	username = db.StringField()
	password = db.StringField()
	#username_index = db.Index().ascending('username').unique()

