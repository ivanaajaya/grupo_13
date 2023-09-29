from ..database import DatabaseConnection
from mysql.connector import Error

class Servidor:
    """Modelo de Servidor"""

    def __init__(self, id_servidor=None, nombre_servidor=None, descripcion=None, cantUser=None):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.cantUser = cantUser

    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "cantUser": self.cantUser
        }

    # @classmethod
    # def obtener_servidor_por_id(cls, id_servidor):
    #     print("entro obtener_servidor_por_id",id_servidor)
    #     try:
    #         query = """SELECT * FROM Servidores WHERE id_servidor = %s"""
    #         params = (id_servidor,)
            
    #         servidor = DatabaseConnection.fetch_one(query,params=params)
    #         print("datos obtenidos del servidor",servidor)
    #         if servidor:
                
    #             return Servidor(servidor[0], servidor[1], servidor[2])
    #         return None
    #     except Exception as e:
    #         print("Error en obtener_servidor_por_id:", e)
    #         return None
    @classmethod
    def obtener_servidores_de_usuario(cls, id_usuario):
        try:
            query = """
                SELECT s.id_servidor, s.nombre_servidor, s.descripcion, s.cantUser
                FROM Servidores s
                INNER JOIN UsuarioServidor us ON s.id_servidor = us.id_servidor
                WHERE us.id_usuario = %s;
            """
            
            params = (id_usuario,)
            
            results = DatabaseConnection.fetch_all(query, params)
            
            servidores = []
            for row in results:
                servidor = cls(*row)
                servidores.append(servidor)
            
            return servidores
        except Exception as e:
            print("Error en obtener_servidores_de_usuario:", e)
            return []

    @classmethod
    def obtener_todos_servidores(cls):
        query = "SELECT * FROM servidores;"
        results = DatabaseConnection.fetch_all(query)

        servidores = []
        if results:
            for result in results:
                servidores.append(cls(*result))
        return servidores

    @classmethod
    def insert_servidor_query(cls, nombre_servidor, descripcion):
        """Esta función se encarga de ejecutar la consulta SQL para insertar un nuevo servidor en la tabla Servidores."""
        try:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            query = """
            INSERT INTO Servidores (nombre_servidor, descripcion, cantUser)
            VALUES (%s, %s, 1)
        """  # Agrega un valor predeterminado para cantUser  # Empezamos con 1 usuario (el administrador)
            params = (nombre_servidor, descripcion)
            cursor.execute(query, params)
            servidor_id = cursor.lastrowid  # Obtenemos el ID del servidor recién insertado
            print("altimo ID---------",servidor_id)
            return servidor_id
        except Exception as e:
            print("Error en crear_servidor:", e)
            return False
        
    @classmethod
    def servidor_existe(cls, servidor_id):
        """para verificar si un servidor existe"""
        try:
            # conn = DatabaseConnection.get_connection()
            # cursor = conn.cursor()
            query = """
            SELECT id_servidor FROM Servidores
            WHERE id_servidor = %s
            """
            params = (servidor_id,)
            # cursor.execute(query, params)
            result = DatabaseConnection.fetch_one(query, params)
            print("paso por el servidor_existe....", bool(result))
            return bool(result)  # Devuelve True si se encuentra el servidor, False si no
        except Exception as e:
            print("Error en servidor_existe:", e)
            return False
        # finally:
        #     cursor.close()
        #     conn.close()
        

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


    @classmethod
    def obtener_servidor_por_id(cls, id_servidor):
        try:
            query = "SELECT * FROM Servidores WHERE id_servidor = %s"
            params = (id_servidor)
            
            servidor = DatabaseConnection.fetch_one(query,params)
            print("datos obtenidos del servidor",servidor)
            if servidor:
                return Servidor(servidor[0], servidor[1], servidor[2])
            return None
        except Exception as e:
            print("Error en obtener_servidor_por_id:", e)
            return None
    
    