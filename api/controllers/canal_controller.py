from ..model.canales_model import Canal
from flask import request, jsonify

class CanalesController:

    # @classmethod
    # def mostrar_canal(cls, canal_id):
    #     try:
    #         canal = Canal.obtener_canal_por_id(canal_id)

    #         if canal:
    #             canal_serializado = canal.serialize()
    #             return jsonify(canal_serializado), 200
    #         else:
    #             return {"mensaje": "Canal no encontrado"}, 404
    #     except Exception as e:
    #         print("Error en mostrar_canal:", e)
    #         return {"mensaje": "Hubo un error en el canal"}, 500

    @classmethod
    def mostrar_canales_por_servidor(cls, servidor_id):
        try:
            canales = Canal.obtener_canales_por_servidor(servidor_id)
            canales_serializados = [canal.serialize() for canal in canales]
            return jsonify(canales_serializados), 200
        except Exception as e:
            print("Error en mostrar_canales_por_servidor:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def crear_canal(cls):
        try:
            data = request.json
            nombre_canal=data.get('nombre_canal', '')
            print(nombre_canal)
            servidor_id=data.get('servidor_id')#servidor_id lo obtiene como un string
            print(servidor_id)
            created_channel =Canal.crear_canal(nombre_canal, servidor_id)
            print (created_channel)
            if created_channel:
                return {'message': 'Canal creado con éxito'}, 200
            else:
                return {'message': 'No se pudo crear el canal'}, 500
        except Exception as e:
            print("Error en crear_canal:", e)
            return {'message': 'Hubo un error en el servidor'}, 500

    # @classmethod
    # def eliminar_canal(cls, canal_id):
    #     try:
    #         deleted_successfully = Canal.eliminar_canal(canal_id)

    #         if deleted_successfully:
    #             return {"message": "Canal eliminado correctamente"}, 204
    #         else:
    #             return {"message": "No se encontró el canal o hubo un problema al eliminarlo"}, 404
    #     except Exception as e:
    #         print("Error en eliminar_canal:", e)
    #         return {"message": "Hubo un error en el servidor"}, 500
