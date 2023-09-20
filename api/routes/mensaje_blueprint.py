from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController

app_blueprint = Blueprint('app_blueprint', __name__)

# Rutas para mensajes
app_blueprint.route('/mensajes', methods=['GET'])(MensajeController.get_todos_mensajes)
app_blueprint.route('/mensajes/<int:mensaje_id>', methods=['GET'])(MensajeController.get_mensaje)
app_blueprint.route('/mensajes', methods=['POST'])(MensajeController.create_mensaje)
app_blueprint.route('/mensajes/<int:mensaje_id>', methods=['DELETE'])(MensajeController.delete_mensaje)
