from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import Flask 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://vwiuylbsciwkjp:1513a18759e0de759b59650fa19bf48f38308b06568718dad7006a750fddcd13@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/ddrpdgert9r94n"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False 
db = SQLAlchemy(app)


__tablename__ = "users"

class User(UserMixin, db.Model):
    """ User model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    hashed_pswd = db.Column(db.String(), nullable=False)
   

class Massage(db.Model):
	""" Massage model """
	id = db.Column(db.Integer, primary_key=True)
	msg_db = db.Column(db.String(500), nullable=False)
	user_id = db.Column(db.Integer, nullable=False)
	user_name = db.Column(db.String(), nullable=False)
	time_db = db.Column(db.String(), nullable=False)