def deploy():
    from app import create_app,db
    from flask_migrate import upgrade,migrate,init,stamp

    from models import User, Address, CurrentOrders, History
    from models import Bakery, Goods, CurrentGoods, CookedGoods, GoodsDetails, GoodType, Images 
    from models import Promocodes

    app = create_app()
    app.app_context().push()

    # create database and tables
    db.create_all()

    # migrate the database
    stamp()
    migrate()
    upgrade()

deploy()