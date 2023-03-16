from app import db, create_app
from datetime import date, datetime
from random import randint

from models import User, Address, CurrentOrders, History
from models import Bakery, Goods, CurrentGoods, CookedGoods, GoodsDetails, GoodType, Images 
from models import Promocodes

app = create_app()
app.app_context().push()

def find_and_delete_user(username: str):
	obj = db.session.query(User).filter(User.username == username).first()

	if obj != None:
		print("Found:", username)

		db.session.delete(obj)
		db.session.commit()

		obj = db.session.query(User).filter(User.username == "Sarzhanchok2").first()

		if obj == None:
			print(username, 'successfuly deleted')
			print()
		else:
			print(username, "wasnt deleted?")
			exit()

	else:
		print(username, 'doesnt exist')
		print()

def delete_all_objects(Class_arg):
	objects = Class_arg.query.all()

	for obj in objects:
		db.session.delete(obj)

	db.session.commit()

find_and_delete_user("Sarzhanchok2")