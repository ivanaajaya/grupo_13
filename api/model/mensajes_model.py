from ..database import DatabaseConnection
from mysql.connector import Error

class Mensaje:
    """Modelo de Mensaje"""

    def __init__(self, id_mensaje=None, contenido=None, fecha_mensaje=None, id_usuario=None, id_canal=None):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.fecha_mensaje = fecha_mensaje
        self.id_usuario = id_usuario
        self.id_canal = id_canal

    def serialize(self):
        return {
            "id_mensaje": self.id_mensaje,
            "contenido": self.contenido,
            "fecha_mensaje": str(self.fecha_mensaje),
            "id_usuario": self.id_usuario,
            "id_canal": self.id_canal,
        }

    @classmethod
    def obtener_mensaje_por_id(cls, mensaje_id):
        query = "SELECT id_mensaje, contenido, fecha_mensaje, id_usuario, id_canal FROM mensajes WHERE id_mensaje = %s"
        params = (mensaje_id,)
        result = DatabaseConnection.fetch_one(query, params)

        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def obtener_mensajes_por_canal(cls, canal_id):
        query = "SELECT id_mensaje, contenido, fecha_mensaje, id_usuario, id_canal FROM mensajes WHERE id_canal = %s"
        params = (canal_id,)
        results = DatabaseConnection.fetch_all(query, params)

        mensajes = []
        if results:
            for result in results:
                mensajes.append(cls(*result))
        return mensajes

    @classmethod
    def obtener_mensajes_de_canal(cls, canal_id):
        try:
            query = """
                
                SELECT m.contenido, m.fecha_mensaje, u.alias, m.id_canal, m.id_usuario
                FROM mensajes m
                INNER JOIN Usuarios u ON m.id_usuario = u.id_usuario
                WHERE m.id_canal = %s
                ORDER BY m.fecha_mensaje ASC;

            """
            params = (canal_id,)
            
            results = DatabaseConnection.fetch_all(query, params)
            
            mensajes = []
            for row in results:
                mensaje = cls(*row)
                mensajes.append(mensaje)
            
            return mensajes
        except Exception as e:
            print("Error en obtener_mensajes_de_canal:", e)
            return []


    @classmethod
    def crear_mensaje(cls, contenido, id_usuario, id_canal):
        try:
            query = "INSERT INTO mensajes (contenido, id_usuario, id_canal) VALUES ( %s, %s, %s);"
            params = (contenido, id_usuario, id_canal)
            result = DatabaseConnection.execute_query(query, params)
            if result:
                print("resultado de admin_query.-----------",result)
                return True
        except Error as e:
            print(f"Error al crear mensaje: {e}")
            return False

    @classmethod
    def eliminar_mensaje(cls, mensaje_id):
        query = "DELETE FROM mensajes WHERE id_mensaje = %s;"
        params = (mensaje_id,)

        try:
            result = DatabaseConnection.execute_query(query, params)
            return True if result else False
        except Error as e:
            print(f"Error al eliminar mensaje: {e}")
            return False
