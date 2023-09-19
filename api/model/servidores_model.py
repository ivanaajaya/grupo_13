from ..database import DatabaseConnection
from mysql.connector import Error
class Servidor:
    """Modelo de Película"""

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
    def get_servidor(cls, servidor):
        query = """SELECT id_servidor, nombre_servidor, fecha_creacion, descripcion, id_usuario FROM proyecto_db.servidores WHERE id_servidor = %s"""
        params = servidor,
        result = DatabaseConnection.fetch_one(query, params=params)
        return cls(*result)
    # En la clase Servidor
    @classmethod
    def obtener_servidor_por_id(cls, servidor_id):
        query = "SELECT id_servidor, nombre_servidor, fecha_creacion, descripcion, id_usuario FROM proyecto_db.servidores WHERE id_servidor = %s"
        params = (servidor_id,)
        result = DatabaseConnection.fetch_one(query, params)
        
        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def get_todos_servidores(cls):
        query = "SELECT id_servidor, nombre_servidor, fecha_creacion, descripcion, id_usuario FROM proyecto_db.servidores;"
        results = DatabaseConnection.fetch_all(query)

        servidores = []
        if results is not None:
            for result in results:
                servidores.append(cls(*result))
        return servidores
    
    
    @classmethod
    def crear_servidor(cls, nombre_servidor, fecha_creacion, descripcion, id_usuario):
        query = "INSERT INTO proyecto_db.servidores (nombre_servidor, fecha_creacion, descripcion, id_usuario) VALUES (%s, %s, %s, %s);"
        params = (nombre_servidor, fecha_creacion, descripcion, id_usuario)
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return cls(
                id_servidor=result,
                nombre_servidor=nombre_servidor,
                fecha_creacion=fecha_creacion,
                descripcion=descripcion,
                id_usuario=id_usuario,
            )
        else:
            return None

    @classmethod
    def eliminar_servidor(cls, id_servidor):
        cls.remove_foreign_key_constraints(id_servidor)
        query = "DELETE FROM proyecto_db.servidores WHERE id_servidor = %s;"
        params = (id_servidor,)
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False
        
    @classmethod
    def remove_foreign_key_constraints(cls, id_servidor):
        """Elimina las restricciones de clave externa relacionadas con un servidor."""
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")  # Desactiva temporalmente la verificación de FK

            # Elimina las restricciones de clave externa relacionadas con el servidor
            query = "ALTER TABLE canales DROP FOREIGN KEY canales_ibfk_2"
            cursor.execute(query)

            # Restaura la verificación de FK
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        except Error as e:
            # Maneja cualquier error que pueda ocurrir al eliminar las restricciones de FK
            print(f"Error al eliminar restricciones de FK: {e}")
        finally:
            if cursor:
                cursor.close()

