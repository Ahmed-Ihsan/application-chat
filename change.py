from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import *
from application import *

app = Flask(__name__)

def change_db ( usear , password , n ):
	data2 = User.query.filter_by(id=n).update(dict(username=usear))
	db.session.commit()
	data2 = User.query.filter_by(id=n).update(dict(hashed_pswd=password))
	db.session.commit()

change_db(,  ,current_user.id)