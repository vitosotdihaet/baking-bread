from marshmallow import Schema, fields, validate
from api_calls.error import ApiError


fields.Field.default_error_messages = {
	        "required": "MISSING_DATA",
	        "null": "NOT_NULLABLE",
	        "validator_failed": "INVALID_VALUE"
	}


class JsonSchema(Schema):

		error_messages = {
	        "unknown": "UNKNOWN_FIELD"
    	}

		def handle_error(self, exc, data, **kwargs):
			invalid_fields = exc.messages

			for key in invalid_fields:
				if 'Not a valid' in invalid_fields[key][0]:
					invalid_fields[key] = 'INVALID_TYPE'
				else:
					invalid_fields[key] = invalid_fields[key][0]

			raise ApiError(invalid_fields)


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
	quantity = fields.Int(quired=True)


class UpdateGoodSchema(JsonSchema):

	name = fields.Str(validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	available = fields.Boolean()
	previousPrice = fields.Int()
	price = fields.Int()
	weight = fields.Int()
	lifetime = fields.Int()
	description = fields.Str(validate=validate.Length(min=1, max=200, error='INVALID_LENGTH'))
	quantity = fields.Int()
