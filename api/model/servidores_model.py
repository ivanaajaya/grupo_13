from ..database import DatabaseConnection
from mysql.connector import Error

class Servidor:
    """Modelo de Servidor"""

    def __init__(self, id_servidor=None, nombre_servidor=None, fecha_creacion=None, descripcion=None, id_usuario=None):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.id_usuario = id_usuario

    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "fecha_creacion": self.fecha_creacion,
            "descripcion": self.descripcion,
            "id_usuario": self.id_usuario,
        }

    @classmethod
    def obtener_servidor_por_id(cls, servidor_id):
        query = "SELECT id_servidor, nombre_servidor, fecha_creacion, descripcion, id_usuario FROM servidores WHERE id_servidor = %s"
        params = (servidor_id,)
        result = DatabaseConnection.fetch_one(query, params)

        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def obtener_todos_servidores(cls):
        query = "SELECT id_servidor, nombre_servidor, fecha_creacion, descripcion, id_usuario FROM servidores;"
        results = DatabaseConnection.fetch_all(query)

        servidores = []
        if results:
            for result in results:
                servidores.append(cls(*result))
        return servidores

    @classmethod
    def crear_servidor(cls, nombre_servidor, fecha_creacion, descripcion, id_usuario):
        query = "INSERT INTO servidores (nombre_servidor, fecha_creacion, descripcion, id_usuario) VALUES (%s, %s, %s, %s);"
        params = (nombre_servidor, fecha_creacion, descripcion, id_usuario)

        try:
            result = DatabaseConnection.execute_query(query, params)
            if result:
                return cls(
                    id_servidor=result.lastrowid,  # Obtener el ID del servidor recién creado
                    nombre_servidor=nombre_servidor,
                    fecha_creacion=fecha_creacion,
                    descripcion=descripcion,
                    id_usuario=id_usuario,
                )
            else:
                return None
        except Error as e:
            print(f"Error al crear servidor: {e}")
            return None

    @classmethod
    def eliminar_servidor(cls, id_servidor):
        cls.quitar_restricciones_clave_foranea(id_servidor)
        query = "DELETE FROM servidores WHERE id_servidor = %s;"
        params = (id_servidor,)

        try:
            result = DatabaseConnection.execute_query(query, params)
            return True if result else False
        except Error as e:
            print(f"Error al eliminar servidor: {e}")
            return False

    @classmethod
    def quitar_restricciones_clave_foranea(cls, id_servidor):
        """Elimina temporalmente las restricciones de clave externa relacionadas con un servidor."""
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")  # Desactiva temporalmente la verificación de FK

            # Aquí puedes eliminar las restricciones de clave externa relacionadas con el servidor si es necesario

            # Restaura la verificación de FK
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        except Error as e:
            print(f"Error al eliminar restricciones de FK: {e}")
        finally:
            if cursor:
                cursor.close()


