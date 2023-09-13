from flask import Flask
from config import Config
from .routes.app_blueprint import app_blueprint


def inicializar_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    app.register_blueprint(app_blueprint)
    
    return app