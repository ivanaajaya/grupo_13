from flask import Blueprint
from ..controllers.servidor_controller import ServidoresController

servidores_blueprint = Blueprint('servidores_blueprint', __name__)

servidores_blueprint.route('/servidores', methods=['GET'])(ServidoresController.mostrar_todos_servidores)
servidores_blueprint.route('/servidores/<int:servidor_id>', methods=['GET'])(ServidoresController.mostrar_servidor)
servidores_blueprint.route('/servidores', methods=['POST'])(ServidoresController.crear_servidor)
servidores_blueprint.route('/servidores/<int:servidor_id>', methods=['DELETE'])(ServidoresController.eliminar_servidor)