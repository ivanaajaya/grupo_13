import mysql.connector


class DatabaseConnection:
    _connection = None
    
    #EJEMPLO DE CONEXIÓN 
    
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
            host='localhost',
            user='root',
            port = "3306",
            password='1998Rojo-',
            database='PROYECTO'
        )
        return cls._connection


#EJEMPLO DE MÉTODO DE CLASES

    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None