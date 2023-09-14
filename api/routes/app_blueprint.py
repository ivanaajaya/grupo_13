from flask import Blueprint
<<<<<<< HEAD
from ..controllers.mensaje_controller import App_controller
=======
from ..controllers.servidor_controller import ServidoresController
from ..controllers.controller_app import MensajeController
>>>>>>> ccd23d7e629a38c6a9dad2cdc46fb020acff0204



#EJEMPLO DE ENDPOINTS CON GET, POST, PUT Y DELETE
app_blueprint = Blueprint('App_blueprint', __name__)

app_blueprint.route('/servidores', methods=['GET'])(ServidoresController.mostrar_todos_servidores)
app_blueprint.route('/servidores/<int:servidor_id>', methods=['GET'])(ServidoresController.mostrar_servidor)
app_blueprint.route('/servidores', methods=['POST'])(ServidoresController.crear_servidor)
app_blueprint.route('/servidores/<int:servidor_id>', methods=['DELETE'])(ServidoresController.eliminar_servidor)
#app_blueprint.route('/mensajes/<int:mensaje_id>', methods=['GET'])(MensajeController.get_mensaje)

