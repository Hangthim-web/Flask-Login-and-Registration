from flask import session,render_template,url_for,Blueprint,request,redirect,flash
from app.models.User import User
from app.services.user_services import register_user,authenticate_user
from werkzeug.security import generate_password_hash
auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST":
        user,error = register_user(
            request.form["first_name"],
            request.form['last_name'],
            request.form['email'],
            request.form['password'],
            request.form['address'],
        ) 
        if error:
            flash(error,'danger')
            return redirect(url_for('auth.register'))
        flash("Account Created Successfully !",'success')
    return render_template("register.html")

@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user  = authenticate_user(
            request.form['email'],
            request.form['password']
        )
        if user:
            session["user_id"] = user.id
            session['name'] = user.first_name 
            return redirect(url_for('auth.dashboard'))
        
        flash("Invalid email or password",'danger')
        return redirect(url_for('auth.login'))
    
    return render_template('login.html')

@auth_bp.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect(url_for('auth.login'))
    return f"Welcome {session['name']} !"

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

