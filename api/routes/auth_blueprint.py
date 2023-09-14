from flask import Blueprint

from ..controllers.auth_controller import UserController

auth_blueprint = Blueprint('auth_blueprint', __name__)

auth_blueprint.route('/login', methods=['POST'])(UserController.login)#para enviar datos al servidor web para crear o actualizar recursos en el servidor.
auth_blueprint.route('/profile', methods=['GET'])(UserController.show_profile)#ver el perfil
auth_blueprint.route('/logout', methods=['GET'])(UserController.logout)#salir de la session