from ..database import DatabaseConnection
from mysql.connector import Error

class Canal: 
    def __init__(self, id_canal=None, nombre_canal=None, id_rol=None, id_servidor=None):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.id_rol = id_rol
        self.id_servidor = id_servidor

    def serialize(self):
        return {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "id_rol": self.id_rol,
            "id_servidor": self.id_servidor
        }
    
    @classmethod
    def obtener_canal(cls, canal_id):
        query = "SELECT id_canal, nombre_canal, id_rol FROM canales WHERE id_canal = %s"
        params = (canal_id,)
        result = DatabaseConnection.fetch_one(query, params)
        
        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def obtener_todos_canales(cls):
        query = "SELECT id_canal, nombre_canal, id_rol, id_servidor FROM canales;"
        results = DatabaseConnection.fetch_all(query)

        canales = []
        if results is not None:
            for result in results:
                canales.append(cls(*result))
        return canales
    
    
    @classmethod
    def crear_canal (cls, nombre_canal, id_rol):
        query = "INSERT INTO canales (nombre_canal, id_rol) VALUES (%s, %s);"
        params = (nombre_canal, id_rol)

        try:
            result = DatabaseConnection.execute_query(query, params)
            if result:
                return cls(
                    id_canal=result.lastrowid, #Obtener el ID del canal recien creado
                    nombre_canal=nombre_canal,
                    id_rol = id_rol
            )
            else:
                return None

        except Error as e:
            print(f"Error al crear servidor: {e}")
            return None

    @classmethod
    def eliminar_canal(cls, id_canal):
        cls.remove_foreign_key_constraints(id_canal)
        query = "DELETE FROM canales WHERE id_canal = %s;"
        params = (id_canal,)
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False