from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'epk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db  = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'

from hatsu import routes
from hatsu.userpckg.routes import users
from hatsu.basepckg.routes import base

app.register_blueprint(users)
app.register_blueprint(base)