import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.user_test
class TestUser:
	def test_user_object(self, user):
		assert user.id != None
		assert user.name != None
		assert user.email != None
		assert user.password_hash != None
		assert user.balance != None
		assert user.phone != None
		assert user.role == 'client'

		assert user.birthday != None
		assert type(user.birthday) == type(date(1999, 12, 12))


	def test_user_from_database(self, user):
		db.session.add(user)
		db.session.commit()

		user_from_db = db.session.query(user.__class__)
		user_id_match = user.__class__.id == user.id

		found_user = user_from_db.filter(user_id_match).first()

		assert found_user.id == user.id
		assert found_user.name == user.name
		assert found_user.email == user.email
		assert found_user.password_hash == user.password_hash
		assert found_user.name == user.name
		assert found_user.birthday == user.birthday
		assert found_user.phone == user.phone
		assert found_user.role == user.role