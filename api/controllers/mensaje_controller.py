from ..model.mensajes_model import Mensaje
from flask import request, jsonify

class MensajesController:

    @classmethod
    def mostrar_todos_mensajes(cls):
        """Obtener todos los mensajes"""
        mensaje_objects = Mensaje.get_todos_mensajes()
        mensajes = []
        for mensaje in mensaje_objects:
            mensajes.append(mensaje.serialize())
        return mensajes, 200
    
    @classmethod
    def mostrar_mensaje(cls, mensaje_id):
        try:
            mensaje = Mensaje.obtener_mensaje_por_id(mensaje_id)

            if mensaje:
                mensaje_serializado = {
                    "id_mensaje": mensaje.id_mensaje,
                    "contenido": mensaje.contenido,
                    "hora_mensaje": str(mensaje.hora_mensaje),
                    "fecha_mensaje": str(mensaje.fecha_mensaje),
                    "id_usuario": mensaje.id_usuario,
                    "id_canal": mensaje.id_canal
                }
                return mensaje_serializado, 200
            else:
                return {"Mensaje": "Mensaje no encontrado"}, 404
        except Exception as e:
            print("Error en mostrar_mensaje:", e)
            return {"Mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def crear_mensaje(cls):
        try:
            data = request.json

            mensaje = Mensaje(
                contenido=data.get('contenido', ''),
                hora_mensaje=data.get('hora_mensaje', ''),
                fecha_mensaje=data.get('fecha_mensaje', ''),
                id_usuario=data.get('id_usuario', None),
                id_canal=data.get('id_canal', None)
            )

            created_message = Mensaje.crear_mensaje(
                mensaje.contenido,
                mensaje.hora_mensaje,
                mensaje.fecha_mensaje,
                mensaje.id_usuario,
                mensaje.id_canal
            )

            if created_message:
                return {'message': 'Mensaje creado con éxito'}, 201
            else:
                return {'message': 'No se pudo crear el mensaje'}, 500
        except Exception as e:
            print("Error en crear_mensaje:", e)
            return {'message': 'Hubo un error en el servidor'}, 500

    @classmethod
    def eliminar_mensaje(cls, mensaje_id):
        deleted_successfully = Mensaje.eliminar_mensaje(mensaje_id)

        if deleted_successfully:
            return jsonify({"message": "Mensaje eliminado correctamente"}), 204
        else:
            return {"message": "No se encontró el mensaje o hubo un problema al eliminarlo"}, 404
