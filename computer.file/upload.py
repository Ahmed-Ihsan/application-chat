from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import *

data = User_inf.query.filter_by(user_id=id_).update(dict(namberphon=number__phone))
db.session.commit()
data = User_inf.query.filter_by(user_id=id_).update(dict(email=em__ail))
db.session.commit()
data2 = User_inf.query.filter_by(user_id=id_).update(dict(city=ci__ty))
db.session.commit()
data2 = User.query.filter_by(id=id_).update(dict(username=user__name))
db.session.commit()
data2 = User.query.filter_by(id=id_).update(dict(hashed_pswd=pass__word))
db.session.commit()

'''
data1 = User.query.all()
for q in data1:
 print(q.username)
 '''