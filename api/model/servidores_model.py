from ..database import DatabaseConnection

class Servidor: 
    def __init__(self, id_servidor=None, nombre_servidor=None, fecha_creacion=None, descripcion=None, id_usuario=None):
        self.id_servior = id_servidor
        self.nombre_servidor = nombre_servidor
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.id_usuario = id_usuario
