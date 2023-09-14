from flask import Flask #para crear una aplicación web
from flask_cors import CORS #permitir que otros dominios realicen solicitudes HTTP a tu aplicación y es una parte importante de la configuración de seguridad y acceso en aplicaciones web
from config import Config
<<<<<<< HEAD
=======
from .routes.app_blueprint import app_blueprint
>>>>>>> ccd23d7e629a38c6a9dad2cdc46fb020acff0204

# from .routes.app_blueprint import App_Blueprint 
from .routes.auth_blueprint import auth_blueprint

from .database import DatabaseConnection

def inicializar_app():
    """Esta función se encarga de inicializar y configurar la aplicación Flask."""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
<<<<<<< HEAD
    #Esto permite que las solicitudes de origen cruzado compartan cookies y encabezados de autenticación.
    CORS(app, supports_credentials=True)

    # Configura la aplicación con opciones de configuración definidas del objeto Config. 
    app.config.from_object(
        Config
    )
=======
    app.register_blueprint(app_blueprint)
>>>>>>> ccd23d7e629a38c6a9dad2cdc46fb020acff0204
    
    # Configura la clase DatabaseConnection con la configuración de la aplicación Flask.
    DatabaseConnection.set_config(app.config)

    app.register_blueprint(auth_blueprint, url_prefix = '/auth') #todas las rutas definidas en auth_blueprint estarán disponibles bajo el prefijo "/auth".

    return app