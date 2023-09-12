from ..database import DatabaseConnection

class Rol: 
    def __init__(self, id_rol=None, nombre_rol=None, permisos=None, id_usuario=None):
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.permisos = permisos
        self.id_usuario = id_usuario

#crear
#modificar
#mostrar
#eliminar
