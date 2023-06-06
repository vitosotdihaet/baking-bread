import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.cooked_goods_test
class TestCookedGoods:
	def test_cooked_good_object(self, cooked_good, bakery, good):
		assert cooked_good.id != None
		assert cooked_good.good.id == good.id
		assert cooked_good.bakery.id == bakery.id


	def test_cooked_good_from_databaset(self, cooked_good, bakery, good):
		db.session.add(good)
		db.session.add(bakery)
		db.session.add(cooked_good)
		db.session.commit()


		cooked_good_from_db = db.session.query(cooked_good.__class__)

		cooked_good_id_match = cooked_good.__class__.bakery_id == bakery.id 
		found_cooked_good = cooked_good_from_db.filter(cooked_good_id_match).first()

		assert found_cooked_good.id == cooked_good.id
		assert found_cooked_good.bakery_id == bakery.id
		assert found_cooked_good.good_id == good.id