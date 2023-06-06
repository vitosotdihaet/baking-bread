from api.routes.schemas_config import JsonSchema
from marshmallow import fields, validate


class AdminLoginAndSignupSchema(JsonSchema):
	username = fields.Str(required=True, validate=validate.Length(min=1, max=64, error='INVALID_LENGTH'))
	password = fields.Str(required=True, validate=validate.Length(min=1, error='INVALID_LENGTH'))


class UserLoginAndSignupSchema(JsonSchema):
	phoneNumber = fields.Str(required=True, validate=validate.Length(min=1, max=21, error='INVALID_LENGTH'))


class VerifyOTPSchema(JsonSchema):
	uid = fields.Str(required=True, validate=validate.Length(equal=8, error='INVALID_LENGTH'))
	code = fields.Str(required=True, validate=validate.Length(equal=4, error='INVALID_LENGTH'))


class ResendOTPSchema(JsonSchema):
	uid = fields.Str(required=True, validate=validate.Length(equal=8, error='INVALID_LENGTH'))