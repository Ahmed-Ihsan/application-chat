from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgres://vwiuylbsciwkjp:1513a18759e0de759b59650fa19bf48f38308b06568718dad7006a750fddcd13@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/ddrpdgert9r94n"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
	db.create_all()
if __name__ == "__main__":
    with app.app_context():
        main()
