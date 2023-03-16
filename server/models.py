from app import db

class User(db.Model): # has relationships with History, CurrentOrders and Address data-tables
	id = db.Column(db.Integer, primary_key = True)
	history_rel = db.relationship('History', backref='client', lazy='dynamic')
	currentOrders_rel = db.relationship('CurrentOrders', backref='client', lazy='dynamic')
	adresses_rel = db.relationship('Address', backref='client', lazy='dynamic')

	username = db.Column(db.String(64), unique=True)
	email = db.Column(db.String(120), unique=True)
	passwordHash = db.Column(db.String(128))
	balance = db.Column(db.Integer)
	birthday = db.Column(db.DateTime)
	phone = db.Column(db.Integer)
	role = db.Column(db.String(10))
	
	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)

	def __repr__(self): # for debugging (just call the object's name to use this magic method)
		return '<User %r>' % (self.username)

class History(db.Model): # connected to User data-table
	id = db.Column(db.Integer, primary_key = True)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	date = db.Column(db.DateTime)
	totalPrice = db.Column(db.Integer)
	address = db.Column(db.String(100))

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

class Bakery(db.Model): # has a relationship with CookedGoods
	id = db.Column(db.Integer, primary_key = True)
	cookedGoods_rel = db.relationship('CookedGoods', backref='bakery', lazy='dynamic')

	name = db.Column(db.String(30))
	address = db.Column(db.String(100))
	openTime = db.Column(db.DateTime)
	closeTime = db.Column(db.DateTime)

class Goods(db.Model): # has relationships with CurrentGoods, CookedGoods, GoodsDetails and GoodType data-tables
	id = db.Column(db.Integer, primary_key = True)
	currentGoods_rel = db.relationship('CurrentGoods', backref='ordered_good', lazy='dynamic')
	cookedGoods_rel = db.relationship('CookedGoods', backref='coocked_good', lazy='dynamic')

	type_good = db.Column(db.String(20))
	image = db.Column(db.String(200))
	available = db.Column(db.Boolean, default=False)
	price = db.Column(db.Integer)
	previousPrice = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	expirationDate = db.Column(db.DateTime)

class CookedGoods(db.Model): # connected to Goods and Bakery data-tables
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
	bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))

	quantity = db.Column(db.Integer)
	cookedAt = db.Column(db.DateTime)

class CurrentOrders(db.Model): # has a relationship with CurrentGoods data-table and connected to User data-table 
	id = db.Column(db.Integer, primary_key = True)
	currentGoods_rel = db.relationship('CurrentGoods', backref='current_order', lazy='dynamic')

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	date = db.Column(db.DateTime)
	totalPrice = db.Column(db.Integer)
	address = db.Column(db.String(100))
	ended = db.Column(db.Boolean, default=False)
	comments = db.Column(db.String(200))

class CurrentGoods(db.Model): # connected to Goods and CurrentOrders data-tables
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
	order_id = db.Column(db.Integer, db.ForeignKey('current_orders.id'))

class GoodsDetails(db.Model): # has a relationship with Images data-table and connected to Goods data-table 
	id = db.Column(db.Integer, primary_key = True)
	images_rel = db.relationship('Images', backref='current_order', lazy='dynamic')

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))

	description = db.Column(db.String(200))
	images = db.Column(db.String(200))
	quantity = db.Column(db.Integer)
	calories = db.Column(db.Float)
	proteins = db.Column(db.Float)
	carbonhydrates = db.Column(db.Float)

class Images(db.Model): # connected to GoodsDeatils data-table
	id = db.Column(db.Integer, primary_key = True)

	goods_details_id = db.Column(db.Integer, db.ForeignKey('goods_details.id'))
	images = db.Column(db.String(200))

class GoodType(db.Model): # connected to Goods data-table
	id = db.Column(db.Integer, primary_key = True)

	good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))

	title = db.Column(db.String(20))

class Promocodes(db.Model): # has no connections and relationships!
	id = db.Column(db.Integer, primary_key = True)

	name = db.Column(db.String(20))
	discount = db.Column(db.Float)