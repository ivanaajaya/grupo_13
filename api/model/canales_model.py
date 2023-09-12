from ..database import DatabaseConnection

class Canal: 
    def __init__(self, id_canal=None, nombre_canal=None, id_rol=None, id_servidor=None):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.id_rol = id_rol
        self.id_servidor = id_servidor