from flask import Blueprint
from ..controllers.mensaje_controller import App_controller



#EJEMPLO DE ENDPOINTS CON GET, POST, PUT Y DELETE

""""
App_blueprint = Blueprint('App_blueprint', __name__)

App_blueprint.route('/products', methods=['GET'])(App_controller.get_.....)
App_blueprint.route('/products/<int:product_id>', methods=['GET'])(App_controller.get_.....)
App_blueprint.route('/products/<int:product_id>', methods = ['DELETE'])(App_controller.delete_....)
App_blueprint.route('/products', methods=['POST'])(App_controller.create_.....)
App_blueprint.route('/products/<int:product_id>', methods=['PUT'])(App_controller.update_....)
# Definir rutas para actualizar y eliminar productos 

"""