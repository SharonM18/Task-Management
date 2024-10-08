from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
from flask_jwt_extended import JWTManager

mongo = PyMongo()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'SZRDTHFYJGUHILJK'
    app.config.from_object(Config)
    
    mongo.init_app(app)
    jwt.init_app(app)
    with app.app_context():
        from .routes import user_routes, admin_routes
        
        # app.register_blueprint(user_routes.app)
        app.register_blueprint(admin_routes.app)
        
    return app

