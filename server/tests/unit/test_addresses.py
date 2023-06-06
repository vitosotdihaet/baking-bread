import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.address_test
class TestAddress:
	def test_address_object(self, address, user):
		assert address.id != None
		assert address.city != None
		assert address.street != None
		assert address.building != None
		assert address.entrance != None
		assert address.floor != None
		assert address.apt != None
		assert address.comment != None

		assert address.client.id == user.id
		assert address.client.name == user.name


	def test_address_from_database(self, address, user, another_user):
		db.session.add(user)
		db.session.add(another_user)
		db.session.add(address)
		db.session.commit()


		address_from_db = db.session.query(address.__class__)

		# note that we try to find history (by its 'user_id' ForeignKey) as if related to 'another_user', which is not a client for that history (see history() function in tests/conftest.py)
		wrong_user_id_match = address.__class__.user_id == another_user.id 
		found_address = address_from_db.filter(wrong_user_id_match).first()

		assert found_address == None


		address_from_db = db.session.query(address.__class__)
		user_id_match = address.__class__.user_id == user.id

		found_address = address_from_db.filter(user_id_match).first()

		assert found_address.client.id == user.id
		assert found_address.user_id == user.id

		assert found_address.id == address.id
		assert found_address.city == address.city
		assert found_address.street == address.street
		assert found_address.building == address.building
		assert found_address.entrance == address.entrance
		assert found_address.floor == address.floor
		assert found_address.apt == address.apt
		assert found_address.comment == address.comment