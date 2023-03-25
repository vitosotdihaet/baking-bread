import sys
sys.path.insert(0, '../')

import factory
from models import User, Address, CurrentOrders, History
from models import Bakery, Goods, CookedGoods, GoodsDetails, GoodTypes
from models import Promocodes


fake_data = factory.Faker


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)

    name = fake_data('name')
    email = fake_data('email')
    password_hash = fake_data('password')
    balance = 3748
    birthday = fake_data('date_this_century')
    phone = '+2110805081371'
    role = 'client'

    class Meta:
        model = User


class HistoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    
    date = fake_data('date_time_this_decade')
    totalPrice = 2134
    address = fake_data('address')

    class Meta:
        model = History


# class HistoryGoodsFactory(factory.alchemy.SQLAlchemyModelFactory):
#     id = factory.Sequence(lambda n: '%s' % n)

#     class Meta:
#         model = HistoryGoods


class AddressFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    
    city = fake_data('city')
    street = fake_data('street_name')
    building = fake_data('building_number')
    entrance = 4
    floor = 15
    apt = 223
    comment = fake_data('sentence', nb_words = 18)

    class Meta:
        model = Address


class BakeryFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    
    name = fake_data('company')
    address = fake_data('address')
    openTime = fake_data('time_object')
    closeTime = fake_data('time_object')

    class Meta:
        model = Bakery


class GoodsFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    
    goodName = fake_data('word')
    image = fake_data('image_url')
    available =fake_data('pybool')
    price = 728
    previousPrice = 999
    weight = 421
    quantity = 1
    lifetime = 1
    description = fake_data('sentence', nb_words = 18)

    class Meta:
        model = Goods


class CookedGoodsFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    
    quantity = 3
    cookedAt = fake_data('date_time_this_century')

    class Meta:
        model = CookedGoods


class CurrentOrdersFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    
    date = fake_data('date_time_this_century')
    totalPrice = 5423
    address = fake_data('address')
    ended = False
    comments = fake_data('sentence', nb_words = 18)

    class Meta:
        model = CurrentOrders


# class CurrentGoodsFactory(factory.alchemy.SQLAlchemyModelFactory):
#     id = factory.Sequence(lambda n: '%s' % n)

#     class Meta:
#         model = CurrentGoods


class GoodsDetailsFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)

    calories = 3.43
    proteins = 45.3
    carbonhydrates = 2.2

    class Meta:
        model = GoodsDetails


class GoodsTypesFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)

    name = fake_data('word')
    order = factory.Sequence(lambda n: '%s' % n)
    displayName = fake_data('word')
    description = fake_data('sentence', nb_words = 18)

    class Meta:
        model = GoodTypes


class PromocodesFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)

    name = fake_data('sentence', nb_words = 2)
    discount = 0.25

    class Meta:
        model = Promocodes