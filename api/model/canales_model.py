from ..database import DatabaseConnection
from mysql.connector import Error

class Canal:
    """Modelo de Canal"""

    def __init__(self, id_canal=None, nombre_canal=None, fecha_creacion=None, id_servidor=None):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.fecha_creacion = fecha_creacion
        self.id_servidor = id_servidor

    def serialize(self):
        return {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "fecha_creacion": self.fecha_creacion,
            "id_servidor": self.id_servidor,
        }

    @classmethod
    def obtener_canal_por_id(cls, canal_id):
        query = "SELECT id_canal, nombre_canal,fecha_creacion, id_servidor FROM canales WHERE id_canal = %s"
        params = (canal_id,)
        result = DatabaseConnection.fetch_one(query, params)

        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def obtener_canales_por_servidor(cls, servidor_id):
        query = "SELECT * FROM canales WHERE id_servidor = %s"
        params = (servidor_id,)
        results = DatabaseConnection.fetch_all(query, params)

        canales = []
        if results:
            for result in results:
                canales.append(cls(*result))
        return canales

    @classmethod
    def crear_canal(cls, nombre_canal, id_servidor):
        try:
            query = "INSERT INTO canales (nombre_canal, id_servidor) VALUES (%s, %s);"
            params = (nombre_canal, id_servidor)
            result = DatabaseConnection.execute_query(query, params)
            if result:
                return True
        except Error as e:
            print(f"Error al crear canal: {e}")
            return False
        
# return cls(
#                     id_canal=result.lastrowid,
#                     nombre_canal=nombre_canal,
#                     id_servidor=id_servidor,
#                 )

    @classmethod
    def eliminar_canal(cls, canal_id):
        query = "DELETE FROM canales WHERE id_canal = %s;"
        params = (canal_id,)

        try:
            result = DatabaseConnection.execute_query(query, params)
            return True if result else False
        except Error as e:
            print(f"Error al eliminar canal: {e}")
            return False