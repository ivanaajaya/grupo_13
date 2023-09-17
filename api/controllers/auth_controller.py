from ..model.auth.usuarios_model import Usuario

from flask import request, session

class UserController:

# acceso
    @classmethod
    def login(cls):
        data = request.json
        user = Usuario(
            alias = data.get('alias'),
            password = data.get('password')
        )
        
        if Usuario.is_registered(user):
            session['alias'] = data.get('alias')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

# Mostrar perfil
    @classmethod
    def show_profile(cls):
        alias = session.get('alias')
        user = Usuario.get(Usuario(alias = alias))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
# cerrar sesión
    @classmethod
    def logout(cls):
        session.pop('alias', None)
        return {"message": "Sesion cerrada"}, 200

# Registro de nuevo usuario
    @classmethod
    def register(cls):
        data = request.json
        alias = data.get('alias')
        correo_electronico=data.get('correo_electronico')

        # Verificar si el alias ya está en uso
        if Usuario.is_alias_in_use(alias):
            return {"message": "Alias ya está en uso"}, 400
        # Verificar si el correo electrónico ya está en uso
        if Usuario.is_email_in_use(correo_electronico):
            return {"message": "Correo electrónico ya está en uso"}, 400


        # Crear el nuevo usuario
        new_user = Usuario(
            alias=alias,
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            password=data.get('password'),
            correo_electronico= correo_electronico,
            fecha_registro=data.get('fecha_registro'),
            estado_activo=data.get('estado_activo'),
            id_rol=data.get('id_rol')
        )

        if Usuario.create_usuario(new_user):
            return {"message": "Usuario registrado exitosamente"}, 200
        else:
            return {"message": "Error al registrar usuario"}, 500  
        
# Restablece la contraseña
    @classmethod
    def reset_password(cls, alias, new_password):
        """Restablece la contraseña de un usuario existente."""

        # Verificar si el alias existe en la base de datos
        if not Usuario.is_alias_in_use(alias):
            return {"message": "Alias no encontrado"}, 404

        # Llama al método update_password para actualizar la contraseña
        if Usuario.update_password(alias, new_password):
            return {"message": "Contraseña restablecida exitosamente"}, 200
        else:
            return {"message": "Error al restablecer la contraseña"}, 500
