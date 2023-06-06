from app import app
from api.extensions import db
from flask import jsonify, request

from api.routes.auth.controller import admin_required
from api.routes.goods.tables_to_json import good_types_json, goods_json
from api.error.error_template import ApiError
from api.routes.goods.schemas import GoodTypeSchema, UpdateGoodTypeSchema, GoodSchema, UpdateGoodSchema
from api.models import GoodTypes, Goods

from pkg.convert_to_json import convert_formdata_to_json


# Admin rights are required to access this endpoint
# This endpoint creates a good type using json from the response
@app.route('/api/good_types', methods=['POST'])
@admin_required()
def create_good_type():

	json = request.json

	# Validating a json from a request
	# Json validation checks for missing required fields,
	# required types of values in the fields, unknown unnecessary fields
	GoodTypeSchema().validate(json)

	name = json.get('name')
	good_type = GoodTypes.query.filter_by(name=name).first()

	if good_type is not None:
		raise ApiError('GOOD_TYPE_ALREADY_EXISTS', status_code=409)

	# Passing json as a dict of arguments using `**` operator
	good_type = GoodTypes(**json)

	db.session.add(good_type)
	db.session.commit()

	# Response will contain created good type using json serialization via flask-marshmallow
	
	# Query params `field_list` and `expand` only are used in GET methods,
	# so they are set to `None`
	return good_types_json(good_type, is_many=False, field_list=None, expand=None), 201


# This endpoint returns response containing all created good types
@app.route('/api/good_types', methods=['GET'])
def get_good_types():

	# Setting available query params
	available_params = ('sort', 'select', 'expand')
	request_params = request.args

	# Checks for unknown query params
	if len(request_params) != 0:
		for param in request_params:
			if param not in available_params:
				raise ApiError('UNKNOWN_QUERY_PARAM')
	
	sort = request_params.get('sort')

	# Getting sorted good types by their `order` field
	# in ascending or descending order based on sort query param
	# If we get no sort query param, sort='asc' is by default
	if sort == 'asc' or sort == None:
		good_types = GoodTypes.query.order_by(GoodTypes.order).all()
	elif sort == 'desc':
		good_types = GoodTypes.query.order_by(GoodTypes.order.desc()).all()
	else:
		raise ApiError('INVALID_SORT_VALUE')

	if len(good_types) == 0:
		raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)

	# Query param 'select' is responsible for putting only needed fields
	# of good types in the response.
	
	field_list = request_params.get('select')

	# Query param 'expand' is responsible for putting list of goods related to each
	# good type in the response.
	# Also can be used with the query param 'select' like `expand=goods.select=name,id`,
	# but there query param 'select' will be applied to each good in the list of them
	
	expand = request_params.get('expand')

	# Response will contain all good types using json serialization via flask-marshmallow
	
	return good_types_json(good_types, is_many=True, field_list=field_list, expand=expand)


# This endpoint returns response containing created good type by its `id`
@app.route('/api/good_types/<int:id>', methods=['GET'])
def get_good_type_by_id(id):

	# Setting available query params
	available_params = ('select', 'expand')
	request_params = request.args

	# Checks for unknown query params
	if len(request_params) != 0:
		for param in request_params:
			if param not in available_params:
				raise ApiError('UNKNOWN_QUERY_PARAM')
	
	good_type = GoodTypes.query.filter_by(id=id).first()

	if good_type is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)

		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	# Query param 'select' is responsible for putting only needed fields
	# of a good type in the response.
	
	field_list = request_params.get('select')

	# Query param 'expand' is responsible for putting list of goods
	# related to a good type in the response.
	# Also can be used with the query param 'select' like `expand=goods.select=name,id`,
	# but there query param 'select' will be applied to each good in the list of them
	
	expand = request_params.get('expand')

	# Response will contain the requested good type using json serialization via flask-marshmallow
	
	return good_types_json(good_type, is_many=False, field_list=field_list, expand=expand)


# Admin rights are required to access this endpoint
# This endpoint updates created good type by its `id`
@app.route('/api/good_types/<int:id>', methods=['PATCH'])
@admin_required()
def update_good_type(id):
	
	good_type_by_id = GoodTypes.query.filter_by(id=id).first()

	if good_type_by_id is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	json = request.json

	# Because `name` field must be unique,
	# we cannot set any other existing names of good types
	if 'name' in json:
		name = json.get('name')
		good = Goods.query.filter_by(name=name).first()

		if good is not None:
			raise ApiError('GOOD_TYPE_NAME_ALREADY_EXISTS', status_code=409)

	# Validating a json from a request
	# Json validation checks for missing required fields,
	# required types of values in the fields, unknown unnecessary fields
	
	UpdateGoodTypeSchema().validate(json)

	GoodTypes.query.filter_by(id=id).update(json)
	db.session.commit()

	good_type = GoodTypes.query.filter_by(id=id).first()

	# Response will contain updated good type using json serialization via flask-marshmallow
	
	# Query params `field_list` and `expand` only are used in GET methods,
	# so they are set to `None`
	return good_types_json(good_type, is_many=False, field_list=None, expand=None), 200


# Admin rights are required to access this endpoint
# This endpoint deletes all good types
@app.route('/api/good_types', methods=['DELETE'])
@admin_required()
def delete_good_types():

	good_types_deleted = GoodTypes.query.all()
	
	if len(good_types_deleted) == 0 or good_types_deleted == None:
		raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)

	for good_type in good_types_deleted:
		db.session.delete(good_type)

	db.session.commit()

	# Response will contain deleted good type using json serialization via flask-marshmallow
	
	# Query params `field_list` and `expand` only are used in GET methods,
	# so they are set to `None`
	return good_types_json(good_types_deleted, is_many=True, field_list=None, expand=None), 200


# Admin rights are required to access this endpoint
# This endpoint deletes a good type by its `id`
@app.route('/api/good_types/<int:id>', methods=['DELETE'])
@admin_required()
def delete_good_type(id):

	good_type_by_id = GoodTypes.query.filter_by(id=id).first()

	if good_type_by_id is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	db.session.delete(good_type_by_id)
	db.session.commit()

	# Response will contain deleted good type using json serialization via flask-marshmallow
	
	# Query params `field_list` and `expand` only are used in GET methods,
	# so they are set to `None`
	return good_types_json(good_type_by_id, is_many=False, field_list=None, expand=None), 200


# Admin rights are required to access this endpoint
# This endpoint creates a good using form-data from the response
@app.route('/api/good_types/<int:id>/goods', methods=['POST'])
@admin_required()
def create_good(id):
	
	good_type_by_id = GoodTypes.query.filter_by(id=id).first()
	
	if good_type_by_id is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	# Converting form-data from request into simple dict
	formdata = request.form.to_dict(flat=True)

	# Converting from-data into json with valid types of values
	json = convert_formdata_to_json(formdata)

	if len(json) == 0 and 'image' not in request.files:
		raise ApiError('FORMDATA_MUST_CONTAIN_DATA') 

	# Validating a json from a request
	# Json validation checks for missing required fields,
	# required types of values in the fields, unknown unnecessary fields
	
	GoodSchema().validate(json)

	name = json.get('name')
	good = Goods.query.filter_by(name=name).first()

	if good is not None:
		raise ApiError('GOOD_ALREADY_EXISTS', status_code=409)

	# Validating an image given in the form-data
	# Also checks if there is an image in the form-data
	if 'image' in request.files:
		image_file = request.files['image'].read()

		if 'png' not in request.files['image'].filename:
			raise ApiError('IMAGE_MUST_BE_PNG', status_code=422)

		if len(image_file) < 50:
			raise ApiError('INVALID_PNG_IMAGE', status_code=422)

	else:
		raise ApiError('NO_IMAGE_FILE_PROVIDED')

	# Passing json as a dict of arguments using `**` operator
	good = Goods(**json, good_type=good_type_by_id)

	db.session.add(good)
	db.session.commit()

	# Saving the image to static/ folder
	with open(f'./static/images/goodImage{str(good.id)}.png', 'wb') as file:
		file.write(image_file)

	# Setting the absolute path to the image in the static/ folder
	# in the created good
	good.image = f'https://eugenv.ru/static/images/goodImage{str(good.id)}.png'

	db.session.add(good)
	db.session.commit()

	# Response will contain created good using json serialization via flask-marshmallow
	
	# Query param `field_list` is only used in GET methods,
	# so it is set to `None`
	return goods_json(good, is_many=False, field_list=None), 201


# This endpoint returns response containing created goods
@app.route('/api/good_types/goods', methods=['GET'])
def get_goods():

	# Setting available query params
	available_params = ('select')
	request_params = request.args

	# Checks for unknown query params
	if len(request_params) != 0:
		for param in request_params:
			if param not in available_params:
				raise ApiError('UNKNOWN_QUERY_PARAM')

	field_list = request_params.get('select')

	goods = Goods.query.all()

	if len(goods) == 0:
		raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)

	# Response will contain all goods using json serialization via flask-marshmallow
	
	return goods_json(goods, is_many=True, field_list=field_list)


# This endpoint returns response containing created good type by its `id`
@app.route('/api/good_types/goods/<int:id>', methods=['GET'])
def get_good_by_id(id):

	# Setting available query params
	available_params = ('select')
	request_params = request.args

	# Checks for unknown query params
	if len(request_params) != 0:
		for param in request_params:
			if param not in available_params:
				raise ApiError('UNKNOWN_QUERY_PARAM')

	field_list = request_params.get('select')

	good_by_id = Goods.query.filter_by(id=id).first()

	if good_by_id is None:
		goods = Goods.query.all()

		if len(goods) == 0:
			raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_DOESNT_EXIST', status_code=409)

	# Response will contain the requested good using json serialization via flask-marshmallow
	
	return goods_json(good_by_id, is_many=False, field_list=field_list)


# Admin rights are required to access this endpoint
# This endpoint updates created good by its `id`
@app.route('/api/good_types/goods/<int:id>', methods=['PATCH'])
@admin_required()
def update_good(id):

	good_by_id = Goods.query.filter_by(id=id).first()

	if good_by_id is None:
		goods = Goods.query.all()

		if len(goods) == 0:
			raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_DOESNT_EXIST', status_code=409)

	# Converting form-data from request into simple dict
	formdata = request.form.to_dict(flat=True)

	# Converting from-data into json with valid types of values
	json = convert_formdata_to_json(formdata)

	if len(json) == 0 and 'image' not in request.files:
		raise ApiError('FORMDATA_MUST_CONTAIN_DATA') 

	# Validating a json from a request
	# Json validation checks for missing required fields,
	# required types of values in the fields, unknown unnecessary fields
	
	UpdateGoodSchema().validate(json)

	# Because `name` field must be unique,
	# we cannot set any other existing names of goods
	if 'name' in json:
		name = json.get('name')
		good = Goods.query.filter_by(name=name).first()

		if good is not None:
			raise ApiError('GOOD_NAME_ALREADY_EXISTS', status_code=409)

	# Validating an image given in the form-data
	if 'image' in request.files:
		image_file = request.files['image'].read()

		if 'png' not in request.files['image'].filename:
			raise ApiError('IMAGE_MUST_BE_PNG', status_code=422)

		if len(image_file) < 50:
			raise ApiError('INVALID_PNG_IMAGE')

		# Saving the image to static/ folder
		with open(f'./static/images/goodImage{str(id)}.png', 'wb') as file:
			file.write(image_file)

		# It is unnecessary to add again absolute path to a good image like this,
		# json['image'] = f'https://eugenv.ru/static/images/goodImage{str(id)}.png'
		# because it was set when a good had been created

	Goods.query.filter_by(id=id).update(json)
	db.session.commit()

	good = Goods.query.filter_by(id=id).first()

	# Response will contain updated good using json serialization via flask-marshmallow
	
	# Query param `field_list` is only used in GET methods,
	# so it is set to `None`
	return goods_json(good, is_many=False, field_list=None), 200


# Admin rights are required to access this endpoint
# This endpoint deletes all goods
@app.route('/api/good_types/goods', methods=['DELETE'])
@admin_required()
def delete_goods():

	goods_deleted = Goods.query.all()

	if len(goods_deleted) == 0 or goods_deleted == None:
		raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)

	for good in goods_deleted:
		db.session.delete(good)

	db.session.commit()

	# Response will contain deleted goods using json serialization via flask-marshmallow
	
	# Query param `field_list` is only used in GET methods,
	# so it is set to `None`
	return goods_json(goods_deleted, is_many=True, field_list=None), 200


# Admin rights are required to access this endpoint
# This endpoint deletes a good by its `id`
@app.route('/api/good_types/goods/<int:id>', methods=['DELETE'])
@admin_required()
def delete_good(id):

	good_by_id = Goods.query.filter_by(id=id).first()

	if good_by_id is None:
		goods = Goods.query.all()

		if len(goods) == 0:
			raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_DOESNT_EXIST', status_code=409)

	db.session.delete(good_by_id)
	db.session.commit()

	# Response will contain deleted good using json serialization via flask-marshmallow
	
	# Query param `field_list` is only used in GET methods,
	# so it is set to `None`
	return goods_json(good_by_id, is_many=False, field_list=None), 200