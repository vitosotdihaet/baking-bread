import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


class TestPromocodes:
	def test_good_object(self, promocode):
		assert promocode.id != None
		assert promocode.name != None
		assert promocode.discount != None


	def test_promocode_from_database(self, promocode):
		db.session.add(promocode)
		db.session.commit()

		promocode_from_db = db.session.query(promocode.__class__)

		promocode_id_match = promocode.__class__.id == promocode.id 
		found_promocode = promocode_from_db.filter(promocode_id_match).first()	

		assert found_promocode.id == promocode.id
		assert found_promocode.name == promocode.name
		assert found_promocode.discount == promocode.discount