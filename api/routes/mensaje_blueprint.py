from flask import Blueprint
from ..controllers.mensaje_controller import MensajesController

mensaje_blueprint = Blueprint('mensaje_blueprint', __name__)

mensaje_blueprint.route('/mensajes/<int:mensaje_id>', methods=['GET'])(MensajesController.mostrar_mensaje)
mensaje_blueprint.route('/mensajes/canal/<int:canal_id>', methods=['GET'])(MensajesController.mostrar_mensajes_por_canal)
mensaje_blueprint.route('/mensajes/canalcanal/<int:canal_id>', methods=['GET'])(MensajesController.mostrar_mensajes_de_canal)
mensaje_blueprint.route('/mensajes', methods=['POST'])(MensajesController.enviar_mensaje)
mensaje_blueprint.route('/mensajes/<int:mensaje_id>', methods=['DELETE'])(MensajesController.eliminar_mensaje)