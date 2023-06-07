from api.routes.schemas_config import JsonSchema
from marshmallow import fields, validate


class BakerySchema(JsonSchema):
	
	name = fields.Str(required=True,  validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	address = fields.Str(required=True, validate=validate.Length(min=1, max=100, error='INVALID_LENGTH'))
	openTime = fields.Str(required=True, validate=validate.Length(min=1, max=10, error='INVALID_LENGTH'))
	closeTime = fields.Str(required=True, validate=validate.Length(min=1, max=10, error='INVALID_LENGTH'))


class UpdateBakerySchema(JsonSchema):
	
	name = fields.Str(validate=validate.Length(min=1, max=20, error='INVALID_LENGTH'))
	address = fields.Str(validate=validate.Length(min=1, max=100, error='INVALID_LENGTH'))
	openTime = fields.Str(validate=validate.Length(min=1, max=10, error='INVALID_LENGTH'))
	closeTime = fields.Str(validate=validate.Length(min=1, max=10, error='INVALID_LENGTH'))