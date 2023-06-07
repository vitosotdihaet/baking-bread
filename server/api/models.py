from api.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


Column = db.Column

class User(db.Model): # has relationships with History, CurrentOrders and Address data-tables
	id = Column(db.Integer, primary_key = True)
	history = db.relationship('History', backref='client', lazy='dynamic')
	currentOrders = db.relationship('CurrentOrders', backref='client', lazy='dynamic')
	adresses = db.relationship('Address', backref='client', lazy='dynamic')

	name = Column(db.String(64))
	email = Column(db.String(120), unique=True)
	balance = Column(db.Integer)
	birthday = Column(db.Date)
	phone = Column(db.String(21))


class Admin(db.Model):
	id = Column(db.Integer, primary_key = True)

	username = Column(db.String(64), unique=True)
	password_hash = Column(db.String(128))
	
	def hash_password(self, password):
		self.password_hash = generate_password_hash(password=password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


class Address(db.Model): # connected to User data-table
	id = Column(db.Integer, primary_key = True)

	user_id = Column(db.Integer, db.ForeignKey('user.id'))

	city = Column(db.String(20))
	street = Column(db.String(20))
	building = Column(db.String(10))
	entrance = Column(db.Integer)
	floor = Column(db.Integer)
	apt = Column(db.Integer)
	comment = Column(db.String(200))


bakery_goods = db.Table('bakery_goods', # relationship table for Goods and Bakery
	Column('good_id', db.Integer, db.ForeignKey('goods.id')),
	Column('bakery_id', db.Integer, db.ForeignKey('bakery.id'))
)


class CookedGoods(db.Model): # relationship table with extra data (related to cooked goods) for Goods and Bakery
	id = Column(db.Integer, primary_key = True)

	good_id = Column(db.Integer, db.ForeignKey('goods.id'))
	bakery_id = Column(db.Integer, db.ForeignKey('bakery.id'))

	quantity = Column(db.Integer)
	cookedAt = Column(db.DateTime)


class CurrentGoods(db.Model): # relationship table with extra data (related to current goods) for Goods and CurrentOrders
	id = Column(db.Integer, primary_key = True)

	good_id = Column(db.Integer, db.ForeignKey('goods.id'))
	order_id = Column(db.Integer, db.ForeignKey('current_orders.id'))

	quantity = Column(db.Integer)


class HistoryGoods(db.Model): # relationship table with extra data (related to history goods) for Goods and History
	id = Column(db.Integer, primary_key = True)

	good_id = Column(db.Integer, db.ForeignKey('goods.id'))
	history_id = Column(db.Integer, db.ForeignKey('history.id'))

	quantity = Column(db.Integer)


class CurrentOrders(db.Model): # has relationship with Goods via CurrentGoods and connected to User data-table 
	id = Column(db.Integer, primary_key = True)
	currentGoods = db.relationship('Goods', secondary='current_goods', lazy='joined')

	user_id = Column(db.Integer, db.ForeignKey('user.id'))

	date = Column(db.DateTime)
	totalPrice = Column(db.Integer)
	address = Column(db.String(100))
	ended = Column(db.Boolean, default=False)


class History(db.Model): # has relationship with Goods via HistoryGoods and connected to User data-table 
	id = Column(db.Integer, primary_key = True)
	historyGoods = db.relationship('Goods', secondary='history_goods', lazy='joined')

	user_id = Column(db.Integer, db.ForeignKey('user.id'))

	date = Column(db.DateTime)
	totalPrice = Column(db.Integer)
	address = Column(db.String(100))
	comment = Column(db.String(200))


class Bakery(db.Model): # has a relationship with CookedGoods and Goods via bakery_goods
	id = Column(db.Integer, primary_key = True)
	cookedGoods_rel = db.relationship('CookedGoods', backref='bakery', lazy='joined')
	bakeryGoods = db.relationship('Goods', secondary=bakery_goods, lazy='joined')

	name = Column(db.String(30))
	address = Column(db.String(100))
	openTime = Column(db.DateTime)
	closeTime = Column(db.DateTime)


class Goods(db.Model): # has relationships with CurrentGoods, CookedGoods, GoodsDetails and GoodType data-tables
	id = Column(db.Integer, primary_key = True)
	cookedGoods = db.relationship('CookedGoods', backref='good', lazy='dynamic')
	goodsDetails = db.relationship('GoodsDetails', backref='good', lazy='dynamic')

	typeId = Column(db.Integer, db.ForeignKey('good_types.id'))

	name = Column(db.String(20), unique = True, nullable=False)
	image = Column(db.String(200))
	available = Column(db.Boolean, default=False)
	price = Column(db.Integer)
	previousPrice = Column(db.Integer)
	weight = Column(db.Integer)
	lifetime = Column(db.Integer)
	description = Column(db.String(200))
	quantity = Column(db.Integer)


class GoodsDetails(db.Model): # has a relationship with Images data-table and connected to Goods data-table 
	id = Column(db.Integer, primary_key = True)

	good_id = Column(db.Integer, db.ForeignKey('goods.id'))

	calories = Column(db.Float)
	proteins = Column(db.Float)
	carbonhydrates = Column(db.Float)


class GoodTypes(db.Model): # connected to Goods data-table
	id = Column(db.Integer, primary_key = True)

	goods = db.relationship('Goods', backref='good_type', cascade="all,delete", lazy='dynamic')

	name = Column(db.String(20), unique = True, nullable=False)
	description = Column(db.String)
	order = Column(db.Integer)


class Promocodes(db.Model): # has no connections and relationships!
	id = Column(db.Integer, primary_key = True)

	name = Column(db.String(20))
	discount = Column(db.Float)
