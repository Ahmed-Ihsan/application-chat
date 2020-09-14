from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import *

data2 = User.query.filter_by(id=id1_).update(dict(username=username2))
db.session.commit()
data2 = User.query.filter_by(id=id1_).update(dict(hashed_pswd=password))
db.session.commit()


'''
data1 = User.query.all()
for q in data1:
 print(q.username)
 '''