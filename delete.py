from models import *
from sqlalchemy import *

engine = create_engine('postgres://vwiuylbsciwkjp:1513a18759e0de759b59650fa19bf48f38308b06568718dad7006a750fddcd13@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/ddrpdgert9r94n')
'''table name'''
#input_N=input('Enter Teble Name')  
#input_N.__table__.drop(engine)
User.__table__.drop(engine)
Massage.__table__.drop(engine)