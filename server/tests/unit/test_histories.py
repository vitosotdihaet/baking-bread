import pytest
from conftest import config_test
from datetime import date, datetime


db = config_test()


@pytest.mark.history_test
class TestHistory:
	def test_history_object(self, history, user):
		assert history.id != None
		assert history.totalPrice != None
		assert history.address != None

		assert history.date != None
		assert type(history.date) == type(datetime(1999, 12, 12, 12, 12))

		assert history.client.id == user.id
		assert history.client.name == user.name


	def test_history_from_database(self, history, user, another_user):
		db.session.add(user)
		db.session.add(another_user)
		db.session.add(history)
		db.session.commit()


		history_from_db = db.session.query(history.__class__)

		# note that we try to find history (by its 'user_id' ForeignKey) as if related to 'another_user', which is not a client for that history (see history() function in tests/conftest.py)
		wrong_user_id_match = history.__class__.user_id == another_user.id 

		found_history = history_from_db.filter(wrong_user_id_match).first()

		assert found_history == None


		history_from_db = db.session.query(history.__class__)
		user_id_match = history.__class__.user_id == user.id

		found_history = history_from_db.filter(user_id_match).first()

		assert found_history.client.id == user.id
		assert found_history.user_id == user.id

		assert found_history.id == history.id
		assert found_history.totalPrice == history.totalPrice
		assert found_history.date == history.date