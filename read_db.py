from flask import Flask, render_template, request, redirect, url_for, flash 
from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask_socketio import SocketIO, join_room, leave_room, send
app = Flask(__name__)

engine = create_engine('postgres://vwiuylbsciwkjp:1513a18759e0de759b59650fa19bf48f38308b06568718dad7006a750fddcd13@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/ddrpdgert9r94n')
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

'''
ed_user = User(username='ed1', hashed_pswd='Ed Jones')
session.add(ed_user)
session.commit()
'''


#socketio = SocketIO(app, manage_session=False)
'''data=User.query.all()
for r in data:
	print(r.id, r.username )
'''
data=Massage.query.all()
for r in data:
	print(r.id,r.msg_db,r.user_id,r.room)

'''
data=User_inf.query.all()
for r in data:
	print(r.namberphon ,r.email,1111111)
	'''

'''
			admin = User.query.filter_by(id=1).first()
			admin.username = 'my_new123_email'
			db.session.commit()
			admin = User.query.filter_by(id=1).first()
			print(admin.username)
			asd='change'
			admin = User.query.filter_by(id=1).update(dict(username=asd))
			db.session.commit()
			data=User.query.all()
			for r in data:
				print(r.id, r.username )'''

a=session.query(room).all()
for s in a :
	print(s.room , s.room_us)

    