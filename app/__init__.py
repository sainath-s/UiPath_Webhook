from flask import Flask 
from flask_bootstrap import Bootstrap
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

#Creating Flask app
flask_app = Flask(__name__)

#setting the app.config to get data from Config class created in config.py
flask_app.config.from_object(Config)

#Creating a db object

db = SQLAlchemy(flask_app)

#importing routes and Models
from app import routes
from app.models import History

#create a new DB in app folder
db.create_all()