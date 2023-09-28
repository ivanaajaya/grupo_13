from flask import Blueprint
from ..controllers.canal_controller import CanalesController

canal_blueprint = Blueprint('canal_blueprint', __name__)

canal_blueprint.route('/canales/<int:canal_id>', methods=['GET'])(CanalesController.mostrar_canal)
canal_blueprint.route('/canales/servidor/<int:servidor_id>', methods=['GET'])(CanalesController.mostrar_canales_por_servidor)
canal_blueprint.route('/canales', methods=['POST'])(CanalesController.crear_canal)# SI SIRVE, EN EL JSON SE DEBE PASAR EL nombre_canal, id_servidor Y LA RUTA ES http://127.0.0.1:5000/canales 
canal_blueprint.route('/canales/<int:canal_id>', methods=['DELETE'])(CanalesController.eliminar_canal)
