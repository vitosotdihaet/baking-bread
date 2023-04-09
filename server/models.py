from app import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model): # has relationships with History, CurrentOrders and Address data-tables
	id = db.Column(db.Integer, primary_key = True)
	history = db.relationship('History', backref='client', lazy='dynamic')
	currentOrders = db.relationship('CurrentOrders', backref='client', lazy='dynamic')
	adresses = db.relationship('Address', backref='client', lazy='dynamic')

	username = db.Column(db.String(64), unique=True)
	name = db.Column(db.String(64))
	email = db.Column(db.String(120), unique=True)
	password_hash = db.Column(db.String(128))
	balance = db.Column(db.Integer)
	birthday = db.Column(db.Date)
	phone = db.Column(db.String(21))
	role = db.Column(db.String(10))
	
	def hash_password(self, password):
		self.password_hash = generate_password_hash(password=password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self): # for debugging (just call the object's name to use this magic method)
		return '<User %r>' % (self.username)


class Address(db.Model): # connected to User data-table
	id = db.Column(db.Integer, primary_key = True)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	city = db.Column(db.String(20))
	street = db.Column(db.String(20))
	building = db.Column(db.String(10))
	entrance = db.Column(db.Integer)
	floor = db.Column(db.Integer)
	apt = db.Column(db.Integer)
	comment = db.Column(db.String(200))


bakery_goods = db.Table('bakery_goods', # relationship table for Goods and Bakery
	db.Column('good_id', db.Integer, db.ForeignKey('goods.id')),
	db.Column('bakery_id', db.Integer, db.ForeignKey('bakery.id'))
)


class CookedGoods(db.Model): # relationship table with extra data (related to cooked goods) for Goods and Bakery
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
	bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))

	quantity = db.Column(db.Integer)
	cookedAt = db.Column(db.DateTime)


class CurrentGoods(db.Model): # relationship table with extra data (related to current goods) for Goods and CurrentOrders
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
	order_id = db.Column(db.Integer, db.ForeignKey('current_orders.id'))

	quantity = db.Column(db.Integer)


class HistoryGoods(db.Model): # relationship table with extra data (related to history goods) for Goods and History
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
	history_id = db.Column(db.Integer, db.ForeignKey('history.id'))
	quantity = db.Column(db.Integer)


class CurrentOrders(db.Model): # has relationship with Goods via CurrentGoods and connected to User data-table 
	id = db.Column(db.Integer, primary_key = True)
	currentGoods = db.relationship('Goods', secondary='current_goods', lazy='joined')

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	date = db.Column(db.DateTime)
	totalPrice = db.Column(db.Integer)
	address = db.Column(db.String(100))
	ended = db.Column(db.Boolean, default=False)


class History(db.Model): # has relationship with Goods via HistoryGoods and connected to User data-table 
	id = db.Column(db.Integer, primary_key = True)
	historyGoods = db.relationship('Goods', secondary='history_goods', lazy='joined')

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	date = db.Column(db.DateTime)
	totalPrice = db.Column(db.Integer)
	address = db.Column(db.String(100))
	comment = db.Column(db.String(200))


class Bakery(db.Model): # has a relationship with CookedGoods and Goods via bakery_goods
	id = db.Column(db.Integer, primary_key = True)
	cookedGoods_rel = db.relationship('CookedGoods', backref='bakery', lazy='joined')
	bakeryGoods = db.relationship('Goods', secondary=bakery_goods, lazy='joined')

	name = db.Column(db.String(30))
	address = db.Column(db.String(100))
	openTime = db.Column(db.DateTime)
	closeTime = db.Column(db.DateTime)


class Goods(db.Model): # has relationships with CurrentGoods, CookedGoods, GoodsDetails and GoodType data-tables
	id = db.Column(db.Integer, primary_key = True)
	cookedGoods = db.relationship('CookedGoods', backref='good', lazy='dynamic')
	goodsDetails = db.relationship('GoodsDetails', backref='good', lazy='dynamic')

	good_type_id = db.Column(db.Integer, db.ForeignKey('good_types.id'))

	name = db.Column(db.String(20), unique = True, nullable=False)
	image = db.Column(db.String(200))
	available = db.Column(db.Boolean, default=False)
	price = db.Column(db.Integer)
	previousPrice = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	lifetime = db.Column(db.Integer)
	description = db.Column(db.String(200))
	quantity = db.Column(db.Integer)


class GoodsDetails(db.Model): # has a relationship with Images data-table and connected to Goods data-table 
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))

	calories = db.Column(db.Float)
	proteins = db.Column(db.Float)
	carbonhydrates = db.Column(db.Float)


class GoodTypes(db.Model): # connected to Goods data-table
	id = db.Column(db.Integer, primary_key = True)

	goods = db.relationship('Goods', backref='good_type', cascade="all,delete", lazy='dynamic')

	name = db.Column(db.String(20), unique = True, nullable=False)
	description = db.Column(db.String)
	order = db.Column(db.Integer)


class Promocodes(db.Model): # has no connections and relationships!
	id = db.Column(db.Integer, primary_key = True)

	name = db.Column(db.String(20))
	discount = db.Column(db.Float)