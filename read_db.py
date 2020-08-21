from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import *
app = Flask(__name__)

data=User.query.all()
for r in data:
	print(r.id, r.username )

data=Massage.query.all()
for r in data:
	print(r.id,r.msg_db,r.user_id)


data=User_inf.query.all()
for r in data:
	print(r.namberphon ,r.email,1111111)
	
asd='asdad'
admin = User.query.filter_by(id=1).update(dict(username=asd))
db.session.commit()
data=User.query.all()
for r in data:
	print(r.id, r.username )
