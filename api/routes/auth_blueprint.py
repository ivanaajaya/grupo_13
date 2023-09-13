from flask import Blueprint

from ..controllers.auth_controller import UserController

auth_blueprint = Blueprint('auth_bp', __name__)

auth_blueprint.route('/login', methods=['POST'])(UserController.login)
auth_blueprint.route('/profile', methods=['GET'])(UserController.show_profile)
auth_blueprint.route('/logout', methods=['GET'])(UserController.logout)