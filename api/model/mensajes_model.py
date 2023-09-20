from ..database import DatabaseConnection
from mysql.connector import Error

class Mensaje:
    """Modelo de Mensaje"""

    def __init__(self, id_mensaje=None, contenido=None, hora_mensaje=None, fecha_mensaje=None, id_usuario=None, id_canal=None):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.hora_mensaje = hora_mensaje
        self.fecha_mensaje = fecha_mensaje
        self.id_usuario = id_usuario
        self.id_canal = id_canal

    def serialize(self):
        return {
            "id_mensaje": self.id_mensaje,
            "contenido": self.contenido,
            "hora_mensaje": self.hora_mensaje,
            "fecha_mensaje": self.fecha_mensaje,
            "id_usuario": self.id_usuario,
            "id_canal": self.id_canal,
        }

    @classmethod
    def obtener_mensaje_por_id(cls, mensaje_id):
        query = "SELECT id_mensaje, contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal FROM proyecto_db.mensajes WHERE id_mensaje = %s"
        params = (mensaje_id,)
        result = DatabaseConnection.fetch_one(query, params)
        
        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def get_todos_mensajes(cls):
        query = "SELECT id_mensaje, contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal FROM proyecto_db.mensajes;"
        results = DatabaseConnection.fetch_all(query)

        mensajes = []
        if results is not None:
            for result in results:
                mensajes.append(cls(*result))
        return mensajes

    @classmethod
    def crear_mensaje(cls, contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal):
        query = "INSERT INTO proyecto_db.mensajes (contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal) VALUES (%s, %s, %s, %s, %s);"
        params = (contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal)
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return cls(
                id_mensaje=result,
                contenido=contenido,
                hora_mensaje=hora_mensaje,
                fecha_mensaje=fecha_mensaje,
                id_usuario=id_usuario,
                id_canal=id_canal,
            )
        else:
            return None

    @classmethod
    def eliminar_mensaje(cls, id_mensaje):
        query = "DELETE FROM proyecto_db.mensajes WHERE id_mensaje = %s;"
        params = (id_mensaje,)
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False
