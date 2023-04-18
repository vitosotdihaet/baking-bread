from app import db, app
from flask import jsonify, request
# from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from routes.auth import admin_required
from routes.tables_to_json import good_types_json, goods_json
from api_calls.error import ApiError
from api_calls.json_validation import GoodTypeSchema, UpdateGoodTypeSchema, GoodSchema, UpdateGoodSchema
from models import GoodTypes, Goods


@app.route('/api/drop_db', methods=['GET'])
# @admin_required()
def drop_database():

	db.drop_all() # Note: if you drop database, run manage.py in your console

	return jsonify(database_dropped=True), 200


@app.route('/api/good_types', methods=['POST'])
# @admin_required()
def create_good_type():

	json = request.json
	GoodTypeSchema().validate(json)
	name = json.get('name')

	good_type = GoodTypes.query.filter_by(name=name).first()

	if good_type is not None:
		raise ApiError('GOOD_TYPE_ALREADY_EXISTS', status_code=409)

	good_type = GoodTypes(**json)

	db.session.add(good_type)
	db.session.commit()

	return good_types_json(good_type, is_many=False, field_list=None, expand=None), 201


@app.route('/api/good_types', methods=['GET'])
def get_good_types():
	available_params = ('sort', 'select', 'expand')
	request_params = request.args

	if len(request_params) != 0:
		for param in request_params:
			if param not in available_params:
				raise ApiError('INVALID_QUERY_PARAM')
	
	sort = request_params.get('sort')

	if sort == 'asc' or sort == None:
		good_types = GoodTypes.query.order_by(GoodTypes.order).all()
	elif sort == 'desc':
		good_types = GoodTypes.query.order_by(GoodTypes.order.desc()).all()
	else:
		raise ApiError('INVALID_SORT_VALUE')

	if len(good_types) == 0:
		raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)

	field_list = request_params.get('select')
	expand = request_params.get('expand')

	return good_types_json(good_types, is_many=True, field_list=field_list, expand=expand)


@app.route('/api/good_types/<int:id>', methods=['GET'])
def get_good_type_by_id(id):
	available_params = ('select', 'expand')
	request_params = request.args

	if len(request_params) != 0:
		for param in request_params:
			if param not in available_params:
				raise ApiError('INVALID_QUERY_PARAM')
	
	good_type = GoodTypes.query.filter_by(id=id).first()

	if good_type is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)

		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	field_list = request_params.get('select')
	expand = request_params.get('expand')

	return good_types_json(good_type, is_many=False, field_list=field_list, expand=expand)


@app.route('/api/good_types/<int:id>', methods=['PATCH'])
# @admin_required()
def update_good_type(id):
	
	good_type_by_id = GoodTypes.query.filter_by(id=id).first()

	if good_type_by_id is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	json = request.json
	UpdateGoodTypeSchema().validate(json)

	GoodTypes.query.filter_by(id=id).update(json)
	db.session.commit()

	good_type = GoodTypes.query.filter_by(id=id).first()

	return good_types_json(good_type, is_many=False, field_list=None, expand=None), 200


@app.route('/api/good_types', methods=['DELETE'])
# @admin_required()
def delete_good_types():

	good_types_deleted = db.session.query(GoodTypes).all()
	if len(good_types_deleted) == 0 or good_types_deleted == None:
		raise ApiError('NOTHING_TO_DELETE')

	for good_type in good_types_deleted:
		db.session.delete(good_type)

	db.session.commit()

	return jsonify(message='SUCCESS_DELETED_ALL_GOOD_TYPES'), 200


@app.route('/api/good_types/<int:id>', methods=['DELETE'])
# @admin_required()
def delete_good_type(id):

	good_type_by_id = GoodTypes.query.filter_by(id=id).first()

	if good_type_by_id is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	db.session.delete(good_type_by_id)
	db.session.commit()

	return good_types_json(good_type_by_id, is_many=False, field_list=None, expand=None), 200



@app.route('/api/good_types/<int:id>/goods', methods=['POST'])
# @admin_required()
def create_good(id):
	
	good_type_by_id = GoodTypes.query.filter_by(id=id).first()
	
	if good_type_by_id is None:
		good_types = GoodTypes.query.all()

		if len(good_types) == 0:
			raise ApiError('NO_GOOD_TYPES_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_TYPE_DOESNT_EXIST', status_code=409)

	json = request.json
	GoodSchema().validate(json)

	name = json.get('name')
	good = Goods.query.filter_by(name=name).first()

	if good is not None:
		raise ApiError('GOOD_ALREADY_EXISTS', status_code=409)

	good = Goods(**json, good_type=good_type_by_id)

	db.session.add(good)
	db.session.commit()

	return goods_json(good, is_many=False, field_list=None), 201


@app.route('/api/good_types/goods', methods=['GET'])
# @admin_required()
def get_goods():

	field_list = request.args.get('select')
	expand = request.args.get('expand')

	goods = Goods.query.all()

	if len(goods) == 0:
		raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)

	return goods_json(goods, is_many=True, field_list=field_list)


@app.route('/api/good_types/goods/<int:id>', methods=['GET'])
# @admin_required()
def get_good_by_id(id):

	field_list = request.args.get('select')
	expand = request.args.get('expand')

	good_by_id = Goods.query.filter_by(id=id).first()

	if good_by_id is None:
		goods = Goods.query.all()

		if len(goods) == 0:
			raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_DOESNT_EXIST', status_code=409)

	return goods_json(good_by_id, is_many=False, field_list=field_list)


@app.route('/api/good_types/goods/<int:id>', methods=['PATCH'])
# @admin_required()
def update_good(id):

	good_by_id = Goods.query.filter_by(id=id).first()

	if good_by_id is None:
		goods = Goods.query.all()

		if len(goods) == 0:
			raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_DOESNT_EXIST', status_code=409)

	json = request.json
	UpdateGoodSchema().validate(json)

	Goods.query.filter_by(id=id).update(json)
	db.session.commit()

	good = Goods.query.filter_by(id=id).first()

	return goods_json(good, is_many=False, field_list=None), 200


@app.route('/api/good_types/goods', methods=['DELETE'])
# @admin_required()
def delete_goods():

	goods_deleted = db.session.query(Goods).all()
	if len(goods_deleted) == 0 or goods_deleted == None:
		raise ApiError('NOTHING_TO_DELETE')

	for good in goods_deleted:
		db.session.delete(good)

	db.session.commit()

	return jsonify(message='SUCCESS_DELETED_ALL_GOODS'), 200


@app.route('/api/good_types/goods/<int:id>', methods=['DELETE'])
# @admin_required()
def delete_good(id):

	good_by_id = Goods.query.filter_by(id=id).first()

	if good_by_id is None:
		goods = Goods.query.all()

		if len(goods) == 0:
			raise ApiError('NO_GOODS_HAVE_BEEN_ADDED', status_code=409)
			
		raise ApiError('GOOD_DOESNT_EXIST', status_code=409)

	db.session.delete(good_by_id)
	db.session.commit()

	return goods_json(good_by_id, is_many=False, field_list=None), 200
