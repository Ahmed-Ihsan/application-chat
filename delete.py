from models import *
from sqlalchemy import *

engine = create_engine("sqlite:///database/db.sqlite")
'''table name'''
#input_N=input('Enter Teble Name')  
#input_N.__table__.drop(engine)
User.__table__.drop(engine)
Massage.__table__.drop(engine)
User_inf.__table__.drop(engine)
room.__table__.drop(engine)