from api_calls.json_validation.base_schema import JsonSchema
from marshmallow import fields, validate


class GoodTypeSchema(JsonSchema):
	
	name = fields.Str(required=True,  validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	description = fields.Str(required=True, validate=validate.Length(min=1, max=200, error='INVALID_LENGTH'))
	order = fields.Int(required=True)


class UpdateGoodTypeSchema(JsonSchema):
	
	name = fields.Str(validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	description = fields.Str(validate=validate.Length(min=1, max=200, error='INVALID_LENGTH'))
	order = fields.Int()


class GoodSchema(JsonSchema):

	name = fields.Str(required=True,  validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	available = fields.Boolean(required=True)
	previousPrice = fields.Int()
	price = fields.Int(required=True)
	weight = fields.Int(required=True)
	lifetime = fields.Int(required=True)
	description = fields.Str(required=True, validate=validate.Length(min=1, max=200, error='INVALID_LENGTH'))
	quantity = fields.Int(required=True)


class UpdateGoodSchema(JsonSchema):

	name = fields.Str(validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	available = fields.Boolean()
	previousPrice = fields.Int()
	price = fields.Int()
	weight = fields.Int()
	lifetime = fields.Int()
	description = fields.Str(validate=validate.Length(min=1, max=200, error='INVALID_LENGTH'))
	quantity = fields.Int()