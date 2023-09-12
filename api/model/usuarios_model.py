from ..database import DatabaseConnection

class Usuario: 
    def __init__(self, id_usuario=None, alias=None, nombre=None, apellido=None, fecha_nacimiento=None, contraceña=None, correo_electronico=None, fecha_registro=None):
        self.id_usuario = id_usuario
        self.alias = alias
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.contraceña = contraceña
        self.correo_electronico = correo_electronico
        self.fecha_registro = fecha_registro
