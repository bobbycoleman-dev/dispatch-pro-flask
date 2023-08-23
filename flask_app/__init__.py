from os import environ
from flask import Flask
from flask_app.blueprints.main import bp as main
from flask_app.blueprints.auth import bp as auth
from flask_app.blueprints.dist_cents import bp as dcs
from flask_app.blueprints.users import bp as users
from flask_app.blueprints.assets import bp as assets
from flask_app.blueprints.customers import bp as customers
from flask_app.blueprints.navigation import bp as navigation
from flask_app.blueprints.schedules import bp as schedules
from flask_app.extensions import bcrypt, db, login_manager
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")


def create_app():
    """Flask app factory"""

    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(dcs)
    app.register_blueprint(users)
    app.register_blueprint(assets)
    app.register_blueprint(customers)
    app.register_blueprint(navigation)
    app.register_blueprint(schedules)

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from flask_app.models.user import User
        from flask_app.models.distribution_center import DistributionCenter
        from flask_app.models.driver import Driver
        from flask_app.models.truck import Truck
        from flask_app.models.customer import Customer
        from flask_app.models.address import Address
        from flask_app.models.schedule import Schedule

        db.create_all()

    return app
