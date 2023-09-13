from ..model.auth.usuarios_model import Usuario

from flask import request, session

class UserController:

# acceso
    @classmethod
    def login(cls):
        data = request.json
        user = Usuario(
            username = data.get('username'),
            password = data.get('password')
        )
        
        if Usuario.is_registered(user):
            session['username'] = data.get('username')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    """ @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "phone_number": user.phone_number,
                "creation_date": user.creation_date,
                "last_login": user.last_login,
                "status_id": user.status_id,
                "role_id": user.role_id
            }, 200 """

# Mostrar perfil
    @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = Usuario.get(Usuario(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
# cerrar sesión
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200