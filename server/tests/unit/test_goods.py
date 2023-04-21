import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


class TestGoods:
	def test_good_object(self, good):
		assert good.goodName != None
		assert good.image != None
		assert good.available != None
		assert good.price != None
		assert good.previousPrice != None
		assert good.weight != None
		assert good.lifetime != None


	def test_good_from_database(self, good):
		db.session.add(good)
		db.session.commit()

		good_from_db = db.session.query(good.__class__)

		good_id_match = good.__class__.id == good.id 
		found_good = good_from_db.filter(good_id_match).first()	

		assert found_good.id == good.id
		assert found_good.type_name == good.name
		assert found_good.goodName == good.goodName
		assert found_good.image == good.image
		assert found_good.available == good.available
		assert found_good.price == good.price
		assert found_good.previousPrice == good.previousPrice
		assert found_good.weight == good.weight
		assert found_good.lifetime == good.expirationDate