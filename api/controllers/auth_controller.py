from ..model.auth.usuarios_model import Usuario

from flask import request, session
import os
class UserController:

# acceso
    @classmethod
    def login(cls):
        data = request.json
        user = Usuario(
            alias = data.get('alias'),
            password = data.get('password')
        )
        alias = data.get('alias')
        usuario = Usuario.get(Usuario(alias=alias))
        id_usuario = usuario.id_usuario
        
        if Usuario.is_registered(user):
            session['alias'] = data.get('alias')
            session['id_usuario'] = id_usuario
            
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
        correo_electronico = data.get('correo_electronico')
        rutaassets= "../assets/"

        # Verificar si el alias ya está en uso
        if Usuario.is_alias_in_use(alias):
            return {"message": "Alias ya está en uso"}, 400
        # Verificar si el correo electrónico ya está en uso
        if Usuario.is_email_in_use(correo_electronico):
            return {"message": "Correo electrónico ya está en uso"}, 400

        # Verificar que los campos obligatorios no estén vacíos
        if not (alias and correo_electronico and data.get('nombre') and data.get('apellido')
                and data.get('password')):
            return {"message": "Los campos obligatorios deben completarse: alias, correo electrónico, nombre, apellido y password."}, 400

        # Crear el nuevo usuario
        new_user = Usuario(
            alias=alias,
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            password=data.get('password'),
            correo_electronico=correo_electronico,
            estado_activo= True,
            imagen= rutaassets+"jiji.png",
            
        )
# id_rol=data.get('id_rol'),

        if Usuario.create_usuario(new_user):
            return {"message": "Usuario registrado exitosamente"}, 200
        else:
            return {"message": "Error al registrar usuario"}, 500
 
# Restablecer la contraseña por alias
    @classmethod
    def reset_password(cls):
        # Obtener los datos del formulario de cambio de contraseña
        data = request.json
        password = data.get('password')
        new_password = data.get('newPassword')

        # Verificar que se haya proporcionado una nueva contraseña válida
        if not new_password:
            return {"message": "Nueva contraseña no válida"}, 400

        # Obtener el alias del usuario actualmente autenticado (si existe)
        alias = session.get('alias')
        # print("VEEEEER", alias)

        # Verificar si el usuario está autenticado
        if not alias:
            return {"message": "Usuario no autenticado"}, 401

        # Verificar que la contraseña actual sea correcta utilizando check_current_password
        if not Usuario.check_current_password(alias, password):
            return {"message": "Contraseña actual incorrecta"}, 401

        # Actualizar la contraseña del usuario en la base de datos
        if Usuario.update_password(alias, new_password):
            return {"message": "Contraseña actualizada exitosamente"}, 200
        else:
            return {"message": "Error al actualizar la contraseña"}, 500
        
# Modificar perfil de usuario- un uso por cada logeo
    @classmethod
    def update_profile(cls):
        """"""
        # Obtiene el alias del usuario actualmente autenticado
        alias = session.get('alias')
        # print("--------------USUARIOOOO------alias--: ", alias)
        #Verifica si el usuario está autenticado
        if not alias:
            # print("--------------USUARIOOOO------not id_usuario:--: ", alias)
            return {"message": "Usuario no autenticado"}, 401

        # Obtiene los datos enviados en el cuerpo de la solicitud (JSON)
        data = request.json
        # print("-------data-----data----:", data)

        # Obtén el usuario actual de la base de datos
        user = Usuario.get(Usuario(alias=alias))
        # print("---------usuario-----user--- :", user)
        # print("---tipo de dato user.", type(user.alias))
        # print("---tipo de dato data.", type(data["alias"]))
        # print("---contenido user.---------", user.alias)
        # print("---contenido data.", data["alias"])
        # Verifica si el usuario existe
        if not user:
            return {"message": "Usuario no encontrado"}, 404

        # # Verifica si se proporciona un nuevo alias y si es diferente del alias actual
        # if "alias" in data and data["alias"] != alias:
            
        # Actualiza los atributos del usuario con los nuevos valores si se proporcionaron
        if data["alias"] == "":
            user.alias =user.alias
        else:
            if Usuario.is_alias_in_use(data["alias"]): # Verifica si el nuevo alias ya está en uso
                return {"message": "El alias ya está en uso"}, 400
            user.alias = data["alias"]
            
        if data["nombre"] == "":
            user.nombre =user.nombre
        else:
            user.nombre = data["nombre"]
            
        if data["apellido"] == "":
            user.apellido=user.apellido
        else:
            user.apellido = data["apellido"]
            
        if data["fecha_nacimiento"] == "":
            user.fecha_nacimiento=user.fecha_nacimiento
        else:
            user.fecha_nacimiento = data["fecha_nacimiento"]
            
        if data["password"] == "":
            user.password =user.password
        else:
            user.password = data["password"]
            
        if data["correo_electronico"] == "":
            user.correo_electronico=user.correo_electronico
        else:
            if Usuario.is_email_in_use(data["correo_electronico"]):
                return {"message": "El correo electronico ya está en uso"}, 400
            user.correo_electronico = data["correo_electronico"]
            
        if data["estado_activo"] == "":
            user.estado_activo=user.estado_activo
        else:
            user.estado_activo = data["estado_activo"]
            
        if data["imagen"] == user.imagen and data["imagen"] != "":
            user.imagen=user.imagen
        else:
            nombre_archivo = os.path.basename(data["imagen"])
            rutaassets= "../assets/"
            user.imagen = rutaassets+ nombre_archivo
            
        # if "id_rol" not in data: 
        #     user.id_rol=user.id_rol
        # else:
        #     user.id_rol = data["id_rol"]

        # Guarda los cambios en la base de datos utilizando update_usuario
        if Usuario.update_usuario(user):
            return {"message": "Perfil actualizado exitosamente"}, 200
        else:
            return {"message": "Error al actualizar perfil"}, 500
