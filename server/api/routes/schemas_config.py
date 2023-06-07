from marshmallow import Schema, fields
from api.error.error_template import ApiError


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
