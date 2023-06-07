from datetime import timedelta


class Default(object):
	TESTING = False

	JWT_TOKEN_LOCATION = ['cookies']
	JWT_COOKIE_SAMESITE = 'None'
	JWT_COOKIE_CSRF_PROTECT = False
	JWT_COOKIE_SECURE = True
	JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
	JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

	SWAGGER = {
        'uiversion': 3,
        'openapi': '3.0.2'
	}

	DB_NAME = 'bakingbread'
	DB_PASSWORD = 'test3915'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@property
	def SQLALCHEMY_DATABASE_URI(self):
		return f'postgresql+psycopg2://postgres:{self.DB_PASSWORD}@localhost/{self.DB_NAME}'


class Development(Default):
	DB_NAME = 'BakingBread'
	DB_PASSWORD = 'test3915'


class Staging(Default):
	DB_NAME = 'bakingbread'
	DB_PASSWORD = 'test3915'