from ..model.servidores_model import Servidor
from flask import request, jsonify

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
    def mostrar_servidor(cls, servidor_id):
        try:
            servidor = Servidor.obtener_servidor_por_id(servidor_id)

            if servidor:
                servidor_serializado = servidor.serialize()
                return jsonify(servidor_serializado), 200
            else:
                return {"mensaje": "Servidor no encontrado"}, 404
        except Exception as e:
            print("Error en mostrar_servidor:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

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
        try:
            deleted_successfully = Servidor.eliminar_servidor(servidor_id)

            if deleted_successfully:
                return {"message": "Servidor eliminado correctamente"}, 204
            else:
                return {"message": "No se encontró el servidor o hubo un problema al eliminarlo"}, 404
        except Exception as e:
            print("Error en eliminar_servidor:", e)
            return {"message": "Hubo un error en el servidor"}, 500

