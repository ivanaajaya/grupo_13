from ..database import DatabaseConnection

class Mensaje: 
    def __init__(self, id_mensaje=None, contenido=None, hora_mensaje=None, fecha_mensaje=None, id_usuario=None, id_canal=None):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.hora_mensaje = hora_mensaje
        self.fecha_mensaje = fecha_mensaje
        self.id_usuario = id_usuario
        self.id_canal = id_canal