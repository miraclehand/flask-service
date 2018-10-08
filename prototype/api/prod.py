from flask_restful import Resource
from flask import request, jsonify
from prototype.models import Product, Supplier 
from prototype.schemas import product_schema, products_schema, supplier_schema, suppliers_schema

class ProductAPI(Resource):
	def init_product(self, _product, data):
		if data is None: return;

		if 'product_id'   in data: _product.product_id   = data['product_id']
		if 'product_name' in data: _product.product_name = data['product_name']
		if 'description'  in data: _product.description  = data['description']
		if 'supplier_id'  in data: _product.supplier_id  = data['supplier_id']
		if 'quantity'     in data: _product.quantity     = data['quantity']
		if 'price'        in data: _product.price        = data['price']

	def set_product(self, dst, src):
		if hasattr(src, 'product_name'): dst.product_name = src.product_name
		if hasattr(src, 'description'):  dst.description  = src.description
		if hasattr(src, 'supplier_id'):  dst.supplier_id  = src.supplier_id
		if hasattr(src, 'quantity'):     dst.quantity     = src.quantity
		if hasattr(src, 'price'):        dst.price        = src.price

	def __init__(self):
		super(ProductAPI, self).__init__()

	def get(self, product_id=None):
		_product = Product()
		self.init_product(_product, request.get_json())

		if product_id:
			product = Product.query.filter(Product.product_id == product_id).first()
			if product:
				return product_schema.jsonify(product)
			else:
				return 'Not exists product'
		else:
			products = Product.query.all()
		
			return products_schema.jsonify(products)

	#update-task
	def put(self):
		_product = Product()
		self.init_product(_product, request.get_json())

		if _product is None or _product.product_id is None:
			return 'put is required product id'

		product = Product.query.filter(Product.product_id == _product.product_id).first()
		if product:
			self.set_product(product, _product)
			product.save()
			return 'Update product', 201
		else:
			return 'Not Exists product_id', 404

	#add-task
	def post(self):
		_product = Product()
		self.init_product(_product, request.get_json())

		product = Product.query.filter(Product.product_id == _product.product_id).first()
		if product:
			return 'Exists product'
		else:
			_product.save()
			return product_schema.jsonify(_product)

	#delete-task
	def delete(self):
		self.init_product(request.get_json())

		product = Product.query.filter(Product.product_id == self._product_id).first()
		product.remove()
		return 'remove product'


class SupplierAPI(Resource):
	def init_supplier(self, _supplier, data):
		if data is None: return;

		if 'supplier_id'   in data: _supplier.supplier_id   = data['supplier_id']
		if 'supplier_name' in data: _supplier.supplier_name = data['supplier_name']
		if 'contact_fname' in data: _supplier.contact_fname = data['contact_fname']
		if 'contact_lname' in data: _supplier.contact_lname = data['contact_lname']
		if 'contact_title' in data: _supplier.contact_title = data['contact_title']
		if 'address'       in data: _supplier.address       = data['address']
		if 'phone'         in data: _supplier.phone         = data['phone']
		if 'email'         in data: _supplier.email         = data['email']
		if 'description'   in data: _supplier.description   = data['description']

	def set_supplier(self, dst, src):
		if hasattr(src, 'supplier_name'): dst.supplier_name = src.supplier_name
		if hasattr(src, 'contact_fname'): dst.contact_fname = src.contact_fname
		if hasattr(src, 'contact_lname'): dst.contact_lname = src.contact_lname
		if hasattr(src, 'contact_title'): dst.contact_title = src.contact_title
		if hasattr(src, 'address'):       dst.address       = src.address
		if hasattr(src, 'phone'):         dst.phone         = src.phone
		if hasattr(src, 'email'):         dst.email         = src.email
		if hasattr(src, 'description'):   dst.description   = src.description

	def __init__(self):
		super(SupplierAPI, self).__init__()

	def get(self, supplier_id=None):
		_supplier = Supplier()
		self.init_supplier(_supplier, request.get_json())

		if supplier_id:
			supplier = Supplier.query.filter(Supplier.supplier_id == supplier_id).first()
			if supplier:
				return supplier_schema.jsonify(supplier)
			else:
				return 'Not exists supplier'
		else:
			suppliers = Supplier.query.all()
		
			return suppliers_schema.jsonify(suppliers)

	#update-task
	def put(self):
		_supplier = Supplier()
		self.init_supplier(_supplier, request.get_json())

		if _supplier is None or _supplier.supplier_id is None:
			return 'put is required supplier id'

		supplier = Supplier.query.filter(Supplier.supplier_id == _supplier.supplier_id).first()
		if supplier:
			self.set_supplier(supplier, _supplier)
			supplier.save()
			return 'Update supplier', 201
		else:
			return 'Not Exists supplier_id', 404

	#add-task
	def post(self):
		_supplier = Supplier()
		self.init_supplier(_supplier, request.get_json())

		supplier = Supplier.query.filter(Supplier.supplier_id == _supplier.supplier_id).first()
		if supplier:
			return 'Exists suppliers'
		else:
			_supplier.save()
			return supplier_schema.jsonify(_supplier)

	#delete-task
	def delete(self):
		self.init_supplier(request.get_json())

		supplier = Supplier.query.filter(Supplier.supplier_id == self._supplier_id).first()
		supplier.remove()
		return 'remove supplier'

