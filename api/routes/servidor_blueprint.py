from flask import Blueprint
from ..controllers.servidor_controller import ServidoresController

app_blueprint = Blueprint('App_blueprint', __name__)

app_blueprint.route('/servidores', methods=['GET'])(ServidoresController.mostrar_todos_servidores)
app_blueprint.route('/servidores/<int:servidor_id>', methods=['GET'])(ServidoresController.mostrar_servidor)
app_blueprint.route('/servidores', methods=['POST'])(ServidoresController.crear_servidor)
app_blueprint.route('/servidores/<int:servidor_id>', methods=['DELETE'])(ServidoresController.eliminar_servidor)