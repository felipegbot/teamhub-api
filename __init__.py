from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key="6bb7a18fea4c078ea7fd8e682cafde8a64cd564dcfa69b2d18133a81028b17e8"
    login_manager = LoginManager()
    login_manager.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:lipao2002@localhost:5432/flask"

    db.init_app(app)
    migrate.init_app(app, db)

    return app