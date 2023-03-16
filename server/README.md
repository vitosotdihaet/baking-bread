# Baking Bread backend part.

### FOR USE: 

* Install ***Python 3.10*** or higher

* Set virtual envinroment via console in the directory called ***/server*** 
	
	`` 
	cd Your-directory/baking-bread/server
	``

	`` 
	python -m venv venv
	``

	* To activate virtual environment: 
	just run ***activate.bat*** in your console, which is in ***server/venv/Scripts*** directory

* Install all of the ***dependencies***:

	1. Flask
	2. flask-cors
	3. flask-marshmallow
	4. flask-migrate
	5. flask-SQLAlchemy
	6. flask-login
	7. flask-openid
	8. psycopg2
	9. python-dotenv

	* when it is done, doing ``pip freeze`` (while having activated virtual env.) you should see this:

		- alembic==1.10.2
		- click==8.1.3
		- colorama==0.4.6
		- defusedxml==0.7.1
		- Flask==2.2.3
		- Flask-Cors==3.0.10
		- Flask-Login==0.6.2
		- flask-marshmallow==0.14.0
		- Flask-Migrate==4.0.4
		- Flask-OpenID==1.3.0
		- Flask-SQLAlchemy==3.0.3
		- greenlet==2.0.2
		- itsdangerous==2.1.2
		- Jinja2==3.1.2
		- Mako==1.2.4
		- MarkupSafe==2.1.2
		- marshmallow==3.19.0
		- packaging==23.0
		- psycopg2==2.9.5
		- python-dotenv==1.0.0
		- python3-openid==3.2.0
		- six==1.16.0
		- SQLAlchemy==2.0.6
		- typing_extensions==4.5.0
		- Werkzeug==2.2.3


* Install and set up ***postgresql*** 
	* set up a ***password***, while setting up postgresql
	* open ***pgAdmin4.exe***, which comes with postgresql
	* create a new database
	* make sure to set up ***the same password*** and ***the same name of the database*** 
	in line ``app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:test3915@localhost/bakingBread"`` 
	of app.py, where "test3915" is the ***password***, "bakingBread" is ***the name of the database***

# Backend files and directories

* ***.flaskenv*** tells flask where's the app file and sets debugging and other parameters.
* ***app.py*** initializes extensions and other essential variables
* ***manage.py*** creates a database and data-tables, migrates and so upgrades that database
* ***models.py*** contains data-tables
* ***/venv*** contains ***/Scripts*** directory, which contains ***activate.bat*** and python modules, which are installed via pip.
* ***/migrations*** contains single-database configuration for Flask

## Migrating data-tables into database:

* Check if there's directory called ***/migrations*** in the ***/server*** directory:
	* if there isn't, activate virtual environment

	* run ``flask db init`` command in your console (in the ***/server*** directory)

* Then run ***manage.py*** in your console, while having activated virtual environment