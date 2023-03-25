import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.address_test
@pytest.mark.history_test
class TestGoodsDetails:
	def test_good_details_object(self, good_details, good):
		assert good_details.id != None
		assert good_details.calories != None
		assert good_details.proteins != None
		assert good_details.carbonhydrates != None

		assert good_details.good.id == good.id


	def test_good_details_from_database(self, good_details, good):
		db.session.add(good)
		db.session.add(good_details)
		db.session.commit()


		good_details_from_db = db.session.query(good_details.__class__)
		good_id_match = good_details.__class__.good_id == good.id 

		found_good_details = good_details_from_db.filter(good_id_match).first()

		assert found_good_details.id == good_details.id
		assert found_good_details.calories == good_details.calories
		assert found_good_details.proteins == good_details.proteins
		assert found_good_details.carbonhydrates == good_details.carbonhydrates

		assert found_good_details.good.id == good.id
		assert found_good_details.good_id == good.id