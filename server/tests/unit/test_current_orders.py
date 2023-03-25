import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.current_order_test
class TestCurrentOrders:
	def test_current_order_object(self, current_order, user):
		assert current_order.id != None
		assert current_order.date != None
		assert current_order.totalPrice != None
		assert current_order.address != None
		assert current_order.ended != None
		assert current_order.comments != None

		assert current_order.client.id == user.id


	def test_current_order_from_databaset(self, current_order, user):
		db.session.add(user)
		db.session.add(current_order)
		db.session.commit()


		current_order_from_db = db.session.query(current_order.__class__)

		current_order_id_match = current_order.__class__.user_id == user.id 
		found_current_order = current_order_from_db.filter(current_order_id_match).first()

		assert found_current_order.id == current_order.id
		assert found_current_order.date == current_order.date
		assert found_current_order.totalPrice == current_order.totalPrice
		assert found_current_order.address == current_order.address
		assert found_current_order.ended == current_order.ended
		assert found_current_order.comments == current_order.comments

		assert found_current_order.client.id == user.id
		assert found_current_order.user_id == user.id