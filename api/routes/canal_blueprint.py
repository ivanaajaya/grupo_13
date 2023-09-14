from flask import Blueprint
from ..controllers.canal_controller import CanalesController

app_blueprint = Blueprint('app_blueprint', __name__)


#EJEMPLO DE ENDPOINTS CON GET, POST, PUT Y DELETE

app_blueprint.route('/canales', methods=['GET'])(CanalesController.mostrar_todos_canales)
app_blueprint.route('/canales/<int:canal_id>', methods=['GET'])(CanalesController.mostrar_canal)
app_blueprint.route('/canales', methods=['POST'])(CanalesController.crear_canal)
app_blueprint.route('/canales/<int:canal_id>', methods=['DELETE'])(CanalesController.eliminar_canal)
