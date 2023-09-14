from ..model.servidores_model import Servidor
from flask import request, jsonify


class ServidoresController:

    @classmethod
    def mostrar_todos_servidores(cls):
        """Obtener todas las películas"""
        servidor_objects = Servidor.get_todos_servidores(
        )  # Obtiene todos los objetos de película
        servidores = []
        for servidor in servidor_objects:
            # Serializa cada película y la agrega a la lista
            servidores.append(servidor.serialize())
        # Retorna la lista de películas serializadas con un código de estado 200
        return servidores, 200
    
    @classmethod
    def mostrar_servidor(cls, servidor_id):
        try:
            # Llama a un método para obtener los datos del servidor por su ID
            servidor = Servidor.obtener_servidor_por_id(servidor_id)

            if servidor:
                # Si se encontró el servidor, serializa los datos y responde con un código de estado 200
                servidor_serializado = {
                    "id_servidor": servidor.id_servidor,
                    "nombre_servidor": servidor.nombre_servidor,
                    "fecha_creacion": str(servidor.fecha_creacion),
                    "descripcion": servidor.descripcion,
                    "id_usuario": servidor.id_usuario
                }
                return servidor_serializado, 200
            else:
                # Si no se encuentra el servidor, responde con un código de estado 404
                return {"Mensaje": "Servidor no encontrado"}, 404
        except Exception as e:
            # Maneja cualquier error que pueda ocurrir en el servidor
            print("Error en mostrar_servidor:", e)
            return {"Mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def crear_servidor(cls):
        try:
            data = request.json

            servidor = Servidor(
                nombre_servidor=data.get('nombre_servidor', ''),
                fecha_creacion=data.get('fecha_creacion', ''),
                descripcion=data.get('descripcion', ''),
                id_usuario=data.get('id_usuario', None)
            )

            created_server = Servidor.crear_servidor(
                servidor.nombre_servidor,
                servidor.fecha_creacion,
                servidor.descripcion,
                servidor.id_usuario
            )

            if created_server:
                return {'message': 'Servidor creado con éxito'}, 201
            else:
                return {'message': 'No se pudo crear el servidor'}, 500
        except Exception as e:
            print("Error en crear_servidor:", e)
            return {'message': 'Hubo un error en el servidor'}, 500

    @classmethod
    def eliminar_servidor(cls, servidor_id):
        deleted_successfully = Servidor.eliminar_servidor(servidor_id)

        if deleted_successfully:
            return jsonify({"message": "Servidor eliminado correctamente"}), 204
        else:
            return {"message": "No se encontró el servidor o hubo un problema al eliminarlo"}, 404
