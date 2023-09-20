import mysql.connector
from mysql.connector import Error
from config import Config  # Importa tu clase de configuración

class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = mysql.connector.connect(
                    host=Config.DATABASE_HOST,
                    user=Config.DATABASE_USERNAME,
                    port=Config.DATABASE_PORT,
                    password=Config.DATABASE_PASSWORD,
                    database=Config.DATABASE_NAME
                )
            except Error as e:
                print("Error al conectar a la base de datos:", e)
        return cls._connection

    @classmethod
    def set_config(cls, config):
        cls._config = config

    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()

        return cursor

    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)

        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)

        return cursor.fetchone()

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

            
    # @classmethod
    # def insert_data(cls, query, database_name=None, params=None):
    #     cursor = cls.get_connection().cursor()
    #     try:
    #         cursor.execute(query, params)
    #         cls._connection.commit()
    #         print("Datos insertados correctamente.")
    #     except Error as err:
    #         print("Error al insertar datos:", err)
    #     finally:
    #         cursor.close() 
    # # Ejemplo de uso:
    # # query = "INSERT INTO tabla (columna1, columna2) VALUES (%s, %s)"
    # # params = ("valor1", "valor2")
    # # DatabaseConnection.insert_data(query, params)
    
    # @classmethod
    # def delete_data(cls, query, database_name=None, params=None):
    #     cursor = cls.get_connection().cursor()

    #     try:
    #         cursor.execute(query, params)
    #         cls._connection.commit()
    #         print("Datos eliminados correctamente.")
    #     except Error as err:
    #         print("Error al eliminar datos:", err)
    #     finally:
    #         cursor.close()
    # # Ejemplo de uso:
    # # query = "DELETE FROM tabla WHERE columna = %s"
    # # params = ("valor_a_eliminar",)
    # # DatabaseConnection.delete_data(query, params)
