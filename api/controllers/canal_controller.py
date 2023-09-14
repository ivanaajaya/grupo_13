from ..model.canales_model import Canal
from flask import request, jsonify


class CanalesController:

    @classmethod
    def mostrar_todos_canales (cls):
        """Obtener todas las películas"""
        servidor_objects = Canal.get_todos_canales(
        )  
        canales = []
        for servidor in servidor_objects:
            canales.append(servidor.serialize())
        # Retorna la lista serializadas con un código de estado 200
        return canales, 200
    
    @classmethod
    def mostrar_canal(cls, canal_id):
        try:
            canal = Canal.obtener_canal(canal_id)
            # Si se encontró el canal, serializa los datos y responde con un código de estado 200
            if canal:
                canal_serializado = {
                    "id_canal": canal.id_canal,
                    "nombre_canal": canal.nombre_canal,
                    "id_rol": canal.id_rol,
                    "id_servidor": canal.id_servidor
                }
                return canal_serializado, 200
            else:
                # Si no se encuentra el canal, responde con un código de estado 404
                return {"Mensaje": "Canal no encontrado"}, 404
        except Exception as e:
            # Maneja cualquier error que pueda ocurrir en el canal
            print("Error en mostrar_canal:", e)
            return {"Mensaje": "Hubo un error en el canal"}, 500
            

    @classmethod
    def crear_canal(cls):
        try:
            data = request.json

            canal = Canal(
                nombre_canal=data.get('nombre_canal', ''),
                id_rol=data.get('id_rol', ''),
                id_servidor=data.get('id_servidor', None)
            )

            created_canal = Canal.crear_canal(
                canal.nombre_canal,
                canal.id_rol,
                canal.id_servidor
            )

            if created_canal:
                return {'message': 'Canal creado con éxito'}, 201
            else:
                return {'message': 'No se pudo crear el canal'}, 500
        except Exception as e:
            print("Error en crear_canal:", e)
            return {'message': 'Hubo un error en el canal'}, 500

    @classmethod
    def eliminar_canal(cls, canal_id):
        deleted_successfully = Canal.eliminar_canal (canal_id)

        if deleted_successfully:
            return jsonify({"message": "Canal eliminado correctamente"}), 204
        else:
            return {"message": "No se encontró el canal o hubo un problema al eliminarlo"}, 404