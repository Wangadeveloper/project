from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from loan.rdbms.database import Database
from loan.rdbms.bootstrap import bootstrap
from dotenv import load_dotenv
import os

load_dotenv()

bcrypt = Bcrypt()
login_manager = LoginManager()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.getenv(
    "DATA_DIR",
    os.path.join(BASE_DIR, "..", "data")
)

db = Database(data_dir=DATA_DIR)

def create_app():
    app = Flask(__name__)
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("❌ SECRET_KEY not set")

    app.config["SECRET_KEY"] = secret_key
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    bootstrap(db)
    from .routes import main
    app.register_blueprint(main)

    return app
