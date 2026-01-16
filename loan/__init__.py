from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from loan.rdbms.database import Database
from loan.rdbms.bootstrap import bootstrap  # optional: create tables on startup
import os

bcrypt = Bcrypt()
login_manager = LoginManager()

db = Database(data_dir="data")  # ✅ persistent JSON DB

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'

    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    # -----------------------------
    # Bootstrap tables
    # -----------------------------
    bootstrap(db)

    from .routes import main
    app.register_blueprint(main)

    return app
