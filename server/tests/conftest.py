# import sys
# sys.path.insert(0, '../')

import pytest
from app import create_app, db, clear_data_from_database
from factory_models import *


def config_test():
    app = create_app()
    app.app_context().push()

    clear_data_from_database()

    return db


@pytest.fixture(scope='module')
def user():
    return UserFactory.build()


@pytest.fixture(scope='module')
def another_user():
    return UserFactory.build()


@pytest.fixture(scope='module')
def history(user):
    return HistoryFactory.build(client = user)


@pytest.fixture(scope='module')
def address(user):
    return AddressFactory.build(client = user)


@pytest.fixture(scope='module')
def bakery():
    return BakeryFactory.build()


@pytest.fixture(scope='module')
def good():
    return GoodsFactory.build()


@pytest.fixture(scope='module')
def cooked_good(good, bakery):
    return CookedGoodsFactory.build(good = good, bakery = bakery)


@pytest.fixture(scope='module')
def current_order(user):
    return CurrentOrdersFactory.build(client = user)


@pytest.fixture(scope='module')
def current_good(good, current_order):
    return CurrentGoodsFactory.build(good = good, current_order = current_order)


@pytest.fixture(scope='module')
def good_details(good):
    return GoodsDetailsFactory.build(good = good)


@pytest.fixture(scope='module')
def promocode():
    return PromocodesFactory.build()