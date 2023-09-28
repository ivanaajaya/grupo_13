from ..database import DatabaseConnection
from ..model.servidores_model import Servidor
from mysql.connector import Error

class UsuarioServidor:
    def __init__(self, **kwargs):
        self.id_UsuarioServidor = kwargs.get('id_UsuarioServidor')
        self.nombre_rol = kwargs.get('nombre_rol')
        self.fecha_unirse = kwargs.get('fecha_unirse')
        self.id_usuario = kwargs.get("id_usuario")
        self.id_servidor = kwargs.get("id_servidor")

    def serialize(self):
        return {
            "id_UsuarioServidor": self.id_UsuarioServidor,
            "nombre_rol": self.nombre_rol,
            'fecha_unirse':self.fecha_unirse,
            "id_usuario": self.id_usuario,
            "id_servidor": self.id_servidor,
        }
        
    @classmethod
    def insert_admin_query(cls, nombre_rol, id_usuario, id_servidor):
        """ Esta función se encarga de ejecutar la consulta SQL para insertar un nuevo registro en la tabla UsuarioServidor"""
        try:
            query = """INSERT INTO UsuarioServidor (nombre_rol, id_usuario, id_servidor)
            VALUES (%s, %s, %s)
        """
            params = (nombre_rol, id_usuario, id_servidor)
            result = DatabaseConnection.execute_query(query, params)
            if result:
                print("resultado de admin_query.-----------",result)
                return True
        except Exception as e:
            print("Error en crear_miembro_servidor:", (e))
            return False
        
    @classmethod
    def insertar_miembro(cls, nombre_rol, id_usuario, id_servidor):
        """para agregar un nuevo miembro a un servidor."""
        try:
            # conn = DatabaseConnection.get_connection()
            # cursor = conn.cursor()
            query = """
            INSERT INTO UsuarioServidor (nombre_rol, id_usuario, id_servidor)
            VALUES (%s, %s, %s)
            """
            params = (nombre_rol, id_usuario, id_servidor)
            result = DatabaseConnection.execute_query(query, params)
            if result:
                # conn.commit()
                print("paso por el insertar_miembro TRUE", result)
                return True
        except Exception as e:
            print("Error en insertar_miembro:", e)
            print("paso por el insertar_miembro FALSE")
            return False
        # finally:
        #     cursor.close()
        #     conn.close()
    
    @classmethod
    def es_miembro(cls, id_servidor, id_usuario):
        """si un usuario es miembro de un servidor"""
        try:
            # conn = DatabaseConnection.get_connection()
            # cursor = conn.cursor()
            query = """
            SELECT id_UsuarioServidor FROM UsuarioServidor
            WHERE id_usuario = %s AND id_servidor = %s
            """
            params = (id_usuario, id_servidor)
            # cursor.execute(query, params)
            result = DatabaseConnection.fetch_one(query, params)
            print("paso por es_miembro", result)
            if result is not None:
                print("paso por es_miembro TRUE")
                return True
            print("paso por es_miembro FALSE")
            return False  # Devuelve True si se encuentra el registro, False si no
        except Exception as e:
            print("Error en es_miembro:", e)
        # finally:
        #     cursor.close()
        #     conn.close()
        
        
    @classmethod
    def obtener_servidores_del_usuario(cls, id_usuario):
        try:

        # Paso 1: Obtener los IDs de los servidores a los que pertenece el usuario
            query = "SELECT id_servidor FROM proyecto_db.UsuarioServidor WHERE id_usuario = %s"
            params = (id_usuario,)
            result = DatabaseConnection.fetch_all(query, params=params)
            servidores_ids = [row[0] for row in result] #lista de servidores
            servidores = []
            for server_id in servidores_ids:
            # Utiliza el método obtener_servidor_por_id de la clase Servidor
                server = Servidor.obtener_servidor_por_id(server_id)
                if server:
                # Construye un diccionario con los detalles del servidor
                    server_details = {
                        'id_servidor': server.id_servidor,
                        'nombre_servidor': server.nombre_servidor,
                        'descripcion': server.descripcion,
                        'cantUser': server.cantUser,
                    }
                    servidores.append(server_details)
            return servidores
        except Exception as e:
            print("Error en obtener_servidores_del_usuario:", e)
            return []

    @classmethod
    def verificar_usuario(cls, id_usuario, id_servidor):
        """"ESTE METODO SI NO ENCONTRO NINGUN REGISTRO RETORNA FALSE """
        try:

            query = "SELECT * FROM proyecto_db.UsuarioServidor WHERE id_usuario = %s AND id_servidor = %s;"
            params = (id_usuario, id_servidor)
            result = DatabaseConnection.fetch_one(query,params)
            # Comprobar si el usuario está registrado en el servidor
            if result is not None:
                return True
            else:
                return False
        except Exception as e:
            print("Error en verificar_usuario:", e)
            return False
