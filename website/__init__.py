from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "migraine.db"

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "heisenberg"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # blueprints
    from .views import views 
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Caretaker

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message = "User needs to be logged in to view this page"
    login_manager.login_message_category = "error"
    login_manager.init_app(app)

    # telling flask how to load a user for login manager
    @login_manager.user_loader
    def load_user(email):
        u = User.query.get(email)
        c = Caretaker.query.get(email)
        app.logger.info('%s user data', u)
        return u or c
    return app

def create_database(app):
    if not path.exists("instance/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("database created")

