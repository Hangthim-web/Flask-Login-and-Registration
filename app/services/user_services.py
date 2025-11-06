from flask import render_template,url_for,Blueprint,request,redirect,flash
from app.models.User import User
from app import db,bcrypt

from werkzeug.security import generate_password_hash
user_bp = Blueprint('users',__name__)


def register_user(first_name,last_name,email,password,address):
    if User.query.filter_by(email=email).first():
        return None,"Email Already Exists !"
        # return redirect(url_for('users.register'))
    
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(first_name=first_name,last_name=last_name,email=email,password=hashed_password,address=address)
    db.session.add(new_user)
    db.session.commit()
    return new_user,None

def authenticate_user(email,password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password,password):
        return user 
    return None
    