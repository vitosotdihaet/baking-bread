def deploy():
    from app import create_app,db
    from flask_migrate import upgrade,migrate,init,stamp

    from models import User, Address, CurrentOrders, History
    from models import Bakery, Goods, CurrentGoods, CookedGoods, GoodsDetails, GoodTypes 
    from models import Promocodes

    import json

    with open("local_db_info.json") as ldi:
        info = json.load(ldi)
        db_name = info.get('name')
        password = info.get('password')

    app = create_app(db_name, password)
    app.app_context().push()

    # create database and tables
    db.create_all()

    # migrate the database
    stamp()
    migrate()
    upgrade()

deploy()