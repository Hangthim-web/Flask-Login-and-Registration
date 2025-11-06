from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:thistimeforsure@localhost/flask_login_register' 

    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)

    from app.routes.users import auth_bp 
    app.register_blueprint(auth_bp)
    return app 


    