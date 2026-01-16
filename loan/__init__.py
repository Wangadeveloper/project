from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from loan.rdbms.database import Database
from loan.rdbms.bootstrap import bootstrap
from config import Config
import os

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    # Ensure writable directories
    os.makedirs(app.config["DATA_DIR"], exist_ok=True)
    os.makedirs(app.config["REPORTS_DIR"], exist_ok=True)

    # Initialize custom DB
    db = Database(data_dir=app.config["DATA_DIR"])
    bootstrap(db)

    # Attach DB to app context
    app.db = db

    from .routes import main
    app.register_blueprint(main)

    return app
