from flask import Blueprint

from ..controllers.auth_controller import UserController

auth_blueprint = Blueprint('auth_blueprint', __name__)

auth_blueprint.route('/login', methods=['POST'])(UserController.login)#para enviar datos al servidor web para crear o actualizar recursos en el servidor.
auth_blueprint.route('/profile', methods=['GET'])(UserController.show_profile)#ver el perfil
auth_blueprint.route('/logout', methods=['GET'])(UserController.logout)#salir de la session
auth_blueprint.route('/register', methods=['POST'])(UserController.register)#registra un usuario 
auth_blueprint.route('/reset', methods=['POST '])(UserController.reset_password)#Restablece la contraseña. POST:  ya que estás enviando datos al servidor para cambiar la contraseña, en lugar de actualizar un recurso completo.
auth_blueprint.route('/update', methods=['PUT'])(UserController.update_profile)#modifica datos del usuario. POST:  ya que estás enviando datos al servidor para cambiar la contraseña, en lugar de actualizar un recurso completo.
