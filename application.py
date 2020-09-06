import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_socketio import SocketIO, join_room, leave_room, send
from werkzeug.utils import secure_filename
from sqlalchemy import *
from wtform_fields import *
from models import *

''' upload imag '''
UPLOAD_FOLDER = os.path.join('static', 'upload')

# Configure app
app = Flask(__name__)
app.secret_key='replace later'
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Configure database
app.config['SQLALCHEMY_DATABASE_URI']="postgres://vwiuylbsciwkjp:1513a18759e0de759b59650fa19bf48f38308b06568718dad7006a750fddcd13@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/ddrpdgert9r94n"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

engine = create_engine("postgres://vwiuylbsciwkjp:1513a18759e0de759b59650fa19bf48f38308b06568718dad7006a750fddcd13@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/ddrpdgert9r94n", pool_size=20, max_overflow=1000)
conn = engine.connect()
conn.close()
# Initialize login manager
login = LoginManager(app)
login.init_app(app)
db.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

socketio = SocketIO(app, manage_session=False)

# Predefined rooms for chat
#ROOMtoS = ["lounge", "news"]

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Update database if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash password
        hashed_pswd = pbkdf2_sha256.hash(password)

        # Add username & hashed password to DB
        user = User(username=username, hashed_pswd=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully. Please login.', 'success')
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    # Allow login if validation success
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        conn.close()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)


@app.route("/logout", methods=['GET'])
def logout():

    # Logout user
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))
    data_msg=Massage.query.all()
    roomto=room.query.all()
    try:
        return render_template("chat.html", username=current_user,rooms=roomto, mas_from_db=data_msg , ro_gl= ro_m)
    except :
        return render_template("chat.html", username=current_user,rooms=roomto, mas_from_db=data_msg , ro_gl= "Lounge")

@app.route("/chatcreate", methods=['GET', 'POST'])
def chatcreate():
    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))
    try:
        room_1=request.form['n']
        us=room(room=room_1 , room_us=current_user.id)
        db.session.add(us)
        db.session.commit()
        data_msg=Massage.query.all()
        roomto=room.query.all()
        return render_template("chat.html", username=current_user, rooms=roomto , mas_from_db=data_msg ,ro_gl= ro_m)
    except Exception as e:
        print(e)
        data_msg=Massage.query.all()
        roomto=room.query.all()
        return render_template("chat.html", username=current_user, rooms=roomto, mas_from_db=data_msg ,ro_gl= ro_m)


@app.route("/chatsend", methods=['GET', 'POST'])
def chatsend(i_d):
    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))
    try:
         if request.method == 'POST':
                f = request.files['file']
                f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
                msg=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
                time_stamp = time.strftime('%b-%d %I:%M%p', time.localtime())
                data=room.query.filter_by(room=i_d).first()
                us=Massage(msg_db=msg , user_id=current_user.id ,user_name=current_user.username , time_db=time_stamp , room=ro_m )
                db.session.add(us)
                db.session.commit()
         data_msg=Massage.query.all()
         roomto=room.query.all()
         return render_template("chat.html", username=current_user, rooms=roomto, mas_from_db=data_msg ,ro_gl= ro_m)
    except Exception as e:
        print(e)
        data_msg=Massage.query.all()
        roomto=room.query.all()
        return render_template("chat.html", username=current_user, rooms=roomto , mas_from_db=data_msg ,ro_gl=ro_m)


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    nexto = 'next'
    nexto_page = '/profile-change'
    data=User_inf.query.filter_by(user_id=current_user.id).first()
    data2=User.query.filter_by(id=current_user.id).first()
    if data != None : 
        return render_template("profile.html",username=data2 , data_pro=data , nexto=nexto ,nexto_page=nexto_page)
    else:
        return render_template("profile.html",username=data2 ,data_pro=data, nexto=nexto,nexto_page=nexto_page)

@app.route("/profile-change", methods=['GET', 'POST'])
def profile_change():
    data=User_inf.query.filter_by(user_id=current_user.id).first()
    data2=User.query.filter_by(id=current_user.id).first()
    if data != None :
       # global user__name , pass__word , number__phone , ci__ty , em__ail
        user__name=request.form['username']
        pass__word=request.form['Password']
        number__phone=request.form['numberphone']
        ci__ty=request.form['city']
        em__ail=request.form['email']
        if user__name == "":
            error="Enter Username "
            nexto_page = '/profile'
            nexto='next'
            return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
        elif pass__word =="":
            nexto='next'
            nexto_page = '/profile'
            error="Enter Your Password"
            return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
        elif em__ail =="":
            nexto='next'
            nexto_page = '/profile'
            error="Enter Your Email"
            return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
        elif ci__ty =="":
            nexto='next'
            nexto_page = '/profile'
            error="Enter Your City"
            return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
        data = User_inf.query.filter_by(user_id=current_user.id).update(dict(namberphon=number__phone))
        db.session.commit()
        data = User_inf.query.filter_by(user_id=current_user.id).update(dict(email=em__ail))
        db.session.commit()
        data2 = User_inf.query.filter_by(user_id=current_user.id).update(dict(city=ci__ty))
        db.session.commit()
        data2 = User.query.filter_by(id=current_user.id).update(dict(username=user__name))
        db.session.commit()
        data2 = User.query.filter_by(id=current_user.id).update(dict(hashed_pswd=pass__word))
        db.session.commit()
        nexto= 'save'
        nexto_page = '/logout'
        data=User_inf.query.filter_by(user_id=current_user.id).first()
        data2=User.query.filter_by(id=current_user.id).first()
        return render_template("profile.html",username=data2 ,data_pro=data, nexto=nexto,nexto_page=nexto_page)
    else:  
            username=request.form['username']
            password=request.form['Password']
            numberphone=request.form['numberphone']
            city=request.form['city']
            email=request.form['email']
            if username == "":
                error="Enter Username "
                nexto_page = '/profile'
                nexto='next'
                return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
            elif password =="":
                nexto='next'
                nexto_page = '/profile'
                error="Enter Your Password"
                return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
            elif email =="":
                nexto='next'
                nexto_page = '/profile'
                error="Enter Your Email"
                return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
            elif city =="":
                nexto='next'
                nexto_page = '/profile'
                error="Enter Your City"
                return render_template('profile.html',error_e=error ,username=data2 ,data_pro=data, nexto=nexto, nexto_page = nexto_page)
            data=[username, password, numberphone , email, city] 
            us=User_inf(namberphon=numberphone , email=email ,city=city, user_id=current_user.id)
            db.session.add(us)
            db.session.commit()
            conn.close()
            nexto = 'save'
            nexto_page = '/logout'
            data=User_inf.query.filter_by(user_id=current_user.id).first()
            data2=User.query.filter_by(id=current_user.id).first()
            conn.close()
            return render_template("profile.html",username=data2 ,data_pro=data, nexto=nexto,nexto_page=nexto_page)
   

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@socketio.on('incoming-msg')
def on_message(data):
        """Broadcast messages"""
        msg = data["msg"]
        username = data["username"]
        room = data["room"]
        # Set timestamp
        time_stamp = time.strftime('%b-%d %I:%M%p', time.localtime())
        # save message in database
        data=User.query.filter_by(username=username).first()
        us=Massage(msg_db=msg , user_id=data.id ,user_name=username ,time_db=time_stamp, room=room)
        db.session.add(us)
        db.session.commit()
        send({"username": username , "msg": msg, "time_stamp": time_stamp}, room=room)


@socketio.on('join')
def on_join(data):
    """User joins a room"""
    global ro_m
    username = data["username"]
    room = data["room"]
    ro_m = data["room"]
    join_room(room)

    # Broadcast that new user has joined
    send({"msg": username + " has joined the " + room + " room."}, room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room"""

    username = data['username']
    room = data['room']
    leave_room(room)
    send({"msg": username + " has left the room"}, room=room)

if __name__ == "__main__":
    socketio.run(app,debug=True)

