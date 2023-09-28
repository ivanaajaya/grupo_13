from ..model.servidores_model import Servidor
from ..model.usuarioservidor_model import UsuarioServidor
from ..model.auth.usuarios_model import Usuario
from ..model.canales_model import Canal
from flask import request, jsonify, session

class ServidoresController:

    @classmethod
    def mostrar_todos_servidores(cls):
        try:
            servidores = Servidor.obtener_todos_servidores()
            servidores_serializados = [servidor.serialize() for servidor in servidores]
            return jsonify(servidores_serializados), 200
        except Exception as e:
            print("Error en mostrar_todos_servidores:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def mostrar_servidores_de_usuario(cls):
        try:
            # Obtener el ID del usuario logeado desde la sesión
            usuario_id = session.get('id_usuario')
            
            # Consultar los servidores en los que el usuario está registrado
            servidores = Servidor.obtener_servidores_de_usuario(usuario_id)
            
            # Si el usuario no está registrado en ningún servidor, devolver un mensaje
            if not servidores:
                return {"mensaje": "El usuario no está registrado en ningún servidor"}, 200
            
            # Serializar los servidores y devolver la respuesta
            servidores_serializados = [servidor.serialize() for servidor in servidores]
            
            return jsonify(servidores_serializados), 200
        except Exception as e:
            print("Error en mostrar_servidores_de_usuario:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def crear_servidor(cls):
        """función principal que utiliza las dos funciones para crear un servidor y asignarle un administrador. """
        try:
            data = request.json
            nombre_servidor = data.get('nombre_servidor', '')
            descripcion = data.get('descripcion')
            id_usuario = session.get('id_usuario')
            print("id de crear servidor", id_usuario)
            # id_usuario = user.id_usuario
            # id_usuario = data.get('id_usuario', None)  # ID del usuario que será administrador,, suponiendo que estás autenticado

            created_server = Servidor.insert_servidor_query(nombre_servidor, descripcion)

            if created_server:
                # Obtener el servidor_id recién creado
                servidor_id = created_server
                # Definir el rol para el creador del servidor (puedes ajustarlo según tus necesidades)
                creador_rol_id = "Administrador"  # Reemplaza esto con el ID del rol "creador" en tu base de datos
                # Crear el registro en miembroServidor
                UsuarioServidor.insert_admin_query(creador_rol_id, id_usuario, servidor_id)
                Canal.crear_canal("#bienvenida", servidor_id)
                print("canal Creado")
                return {'message': 'Servidor creado con éxito'}, 201
            else:
                return {'message': 'No se pudo crear el servidor'}, 500
        except Exception as e:
            print("Error en crear_servidor:", e)
            return {'message': 'Hubo un error en el servidor'}, 500
        
    @classmethod
    def unirse_servidor(cls):
        try:
            data = request.json
            id_servidor = data.get('id_servidor')
            id_usuario = session.get('id_usuario')
            # id_usuario = data.get('id_usuario')  # ID del usuario que quiere unirse al servidor

            # Verificar si el servidor_id es válido y existe en la base de datos
            if not Servidor.servidor_existe(id_servidor):
                return {'message': 'El servidor no existe'}, 404

            # Verificar si el usuario ya es miembro del servidor
            if UsuarioServidor.es_miembro(id_servidor, id_usuario):
                return {'message': 'Ya eres miembro de este servidor'}, 400

            # Definir el rol para el nuevo miembro (puedes ajustarlo según tus necesidades)
            creador_rol_id= "Miembro"  # Reemplaza esto con el ID del rol "miembro" en tu base de datos

            # Crear el registro en UsuarioServidor para el nuevo miembro
            UsuarioServidor.insertar_miembro(creador_rol_id, id_usuario, id_servidor)

            return {'message': 'Te has unido al servidor con éxito'}, 201

        except Exception as e:
            print("Error en unirse_servidor:", e)
            return {'message': 'Hubo un error en el servidor'}, 500
    
    # @classmethod
    # def unirse_a_servidor(cls, servidor_id):
    #     print("Llego a unirse_servidor")
    #     resul=0
    #     try:
    #     # Obtén los datos de la solicitud JSON
    #         data = request.json
    #         user_id = data.get('user_id', None)
    #         print("SERVIDOR ID:", servidor_id, "USUARIO ID:", user_id)
    #         resul = UsuarioServidor.verificar_usuario(user_id, servidor_id)
    #         print(resul)
    #         if resul:
    #             print("Error al unirse al servidor: Usuario ya registrado en el servidor.")
    #             return {'message': 'El usuario ya está registrado en el servidor'}, 400
    #         else:
    #         # Verificar si el usuario se encuentra en la base de datos MiembroServidor con ese server_id
    #         # Si no lo encuentra, lo agrega como miembro
    #             if UsuarioServidor.crear_miembro_servidor(user_id, servidor_id, "miembro"):
    #                 return {'message': 'Usuario asignado al servidor con éxito'}, 200
    #             else:
    #                 return {'message': 'Hubo un error en el servidor'}, 500
    #     except Exception as e:
    #         print("Error al unirse al servidor:", str(e))
    #         return {'message': 'Hubo un error en la solicitud'}, 500

    @classmethod
    def eliminar_servidor(cls, servidor_id):
        try:
            deleted_successfully = Servidor.eliminar_servidor(servidor_id)

            if deleted_successfully:
                return {"message": "Servidor eliminado correctamente"}, 204
            else:
                return {"message": "No se encontró el servidor o hubo un problema al eliminarlo"}, 404
        except Exception as e:
            print("Error en eliminar_servidor:", e)
            return {"message": "Hubo un error en el servidor"}, 500

