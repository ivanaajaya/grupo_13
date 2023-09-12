from ..model.models_app import App
from flask import request, jsonify
from ..model.mensajes_model import Mensaje
from ..database import DatabaseConnection


# -------------- CLASE CONTROLADOR ----------------
#class eJEMPLO:

class App_controller:
    pass 

# ----------MÉTODOS DE CLASE --------------
    # @classmethod 

class MensajeController:

    @classmethod
    def get_mensaje(cls, mensaje_id):
        try:
            mensaje_instance = Mensaje.mostrar_mensaje(mensaje_id)
            if mensaje_instance:
                response_data = {
                    "id": mensaje_instance.id_mensaje,
                    "contenido": mensaje_instance.contenido,
                    "hora_mensaje": mensaje_instance.hora_mensaje,
                    "fecha_mensaje": mensaje_instance.fecha_mensaje,
                    "id_usuario": mensaje_instance.id_usuario,
                    "id_canal": mensaje_instance.id_canal
                }
                return jsonify(response_data), 200
            else:
                return {"Mensaje": "No se encontró el mensaje"}, 404
        except Exception as e:
            print("Error en get_mensaje:", e)
            return {"Mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def create_mensaje(cls):
        try:
            data = request.json

            mensaje = Mensaje(
                contenido=data.get('contenido', ''),
                id_usuario=data.get('id_usuario', None),
                id_canal=data.get('id_canal', None)
            )

            created = Mensaje.crear_mensaje(mensaje)

            if created:
                return {'message': 'Mensaje creado con éxito'}, 201
            else:
                return {'message': 'No se pudo crear el mensaje'}, 500
        except Exception as e:
            print("Error en create_mensaje:", e)
            return {'message': 'Hubo un error en el servidor'}, 500

    @classmethod
    def delete_mensaje(cls, mensaje_id):
        deleted_successfully = Mensaje.eliminar_mensaje(mensaje_id)

        if deleted_successfully:
            return jsonify({"Mensaje": "Mensaje eliminado correctamente"}), 204
        else:
            return {"Mensaje": "No se encontró el mensaje o hubo un problema al eliminarlo"}, 404