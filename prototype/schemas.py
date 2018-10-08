from prototype import db, ma
from marshmallow import missing, post_dump, pre_dump, fields
from prototype.models import Supplier

class BaseSchema(ma.Schema):
	def on_bind_field(self, field_name, field_obj):
		if field_obj.missing == missing:
			field_obj.missing = None
			field_obj_allow_none = True

class ProductSchema(BaseSchema):
	"""
	product_id = fields.Field()
	product_name = fields.Field()
	product_description = fields.Field()
	quantity = fields.Field()
	price = fields.Field()
	"""
	class Meta:
		fields = ('product_id', 'product_name')
	_links = ma.Hyperlinks({
		'self': ma.URLFor('product', product_id='<product_id>'),
		'collection': ma.URLFor('product')
	})

class SupplierSchema(ma.Schema):
	"""
	supplier_id = fields.Field()
	supplier_name = fields.Field()
	email = fields.Field()
	phone = fields.Field()
	"""

	class Meta:
		fields = ('supplier_id', 'supplier_name')

	_links = ma.Hyperlinks({
		'self': ma.URLFor('supplier', supplier_id='<supplier_id>'),
		'collection': ma.URLFor('supplier')
	})

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)

