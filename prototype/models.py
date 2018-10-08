from prototype import db

class User(db.Document):
	username = db.StringField()
	password = db.StringField()
	#username_index = db.Index().ascending('username').unique()
	#i_name_pass= db.Index().ascending('username').descending('password')

class Product(db.Document):
	product_id = db.StringField()
	product_name = db.StringField()
	supplier_id = db.StringField()
	description = db.StringField(required=False)
	quantity = db.IntField(required=False)
	price = db.IntField(required=False)
	#data_created = db.Date(DateTime, auto_now_add=True)

class Supplier(db.Document):
	supplier_id = db.StringField()
	supplier_name = db.StringField()
	contact_fname = db.StringField(required=False)
	contact_lname = db.StringField(required=False)
	contact_title = db.StringField(required=False)
	address = db.StringField(required=False)
	phone = db.StringField(required=False)
	email = db.StringField(required=False)
	description = db.StringField(required=False)

