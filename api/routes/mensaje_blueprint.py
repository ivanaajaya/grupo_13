from flask import Blueprint
from ..controllers.mensaje_controller import MensajesController  # Importa el controlador de mensajes

app_blueprint = Blueprint('mensaje_blueprint', __name__)

app_blueprint.route('/mensajes', methods=['GET'])(MensajesController.mostrar_todos_mensajes)
app_blueprint.route('/mensajes/<int:mensaje_id>', methods=['GET'])(MensajesController.mostrar_mensaje)
app_blueprint.route('/mensajes', methods=['POST'])(MensajesController.crear_mensaje)
app_blueprint.route('/mensajes/<int:mensaje_id>', methods=['DELETE'])(MensajesController.eliminar_mensaje)
