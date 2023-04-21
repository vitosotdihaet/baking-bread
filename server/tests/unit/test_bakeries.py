import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.bakery_test
class TestBakery:
	def test_bakery_object(self, bakery):
		assert bakery.name != None
		assert bakery.address != None
		assert bakery.openTime != None
		assert bakery.closeTime != None


	def test_bakery_from_databaset(self, bakery):
		db.session.add(bakery)
		db.session.commit()


		bakery_from_db = db.session.query(bakery.__class__)

		bakery_id_match = bakery.__class__.id == bakery.id 
		found_bakery = bakery_from_db.filter(bakery_id_match).first()

		assert found_bakery.id == bakery.id
		assert found_bakery.name == bakery.name
		assert found_bakery.address == bakery.address
		assert found_bakery.openTime == bakery.openTime
		assert found_bakery.closeTime == bakery.closeTime