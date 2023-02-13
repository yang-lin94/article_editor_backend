from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.config import Config
from api.resources import main

db = SQLAlchemy()

def create_app():
    '''初始化flask app'''
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main)

    return app
