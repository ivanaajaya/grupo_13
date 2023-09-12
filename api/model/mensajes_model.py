from datetime import datetime

class Mensaje:
    def __init__(self, id_mensaje=None, contenido=None, hora_mensaje=None, fecha_mensaje=None, id_usuario=None, id_canal=None):
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.hora_mensaje = hora_mensaje
        self.fecha_mensaje = fecha_mensaje
        self.id_usuario = id_usuario
        self.id_canal = id_canal

    @classmethod
    def crear_mensaje(cls, contenido, id_usuario, id_canal):
        hora_mensaje = datetime.now().strftime("%H:%M:%S")
        fecha_mensaje = datetime.now().strftime("%Y-%m-%d")

        query = "INSERT INTO mensajes (contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal) VALUES (%s, %s, %s, %s, %s);"
        params = (contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal)

        result = DatabaseConnection.execute_query(query, params)

        if result:
            return cls(
                id_mensaje=result,
                contenido=contenido,
                hora_mensaje=hora_mensaje,
                fecha_mensaje=fecha_mensaje,
                id_usuario=id_usuario,
                id_canal=id_canal,
            )
        else:
            return None

    @classmethod
    def mostrar_mensaje(cls, id_mensaje):
        query = "SELECT * FROM mensajes WHERE id_mensaje = %s;"
        params = (id_mensaje,)

        result = DatabaseConnection.fetch_one(query, params)

        if result:
            return cls(
                id_mensaje=result[0],
                contenido=result[1],
                hora_mensaje=result[2],
                fecha_mensaje=result[3],
                id_usuario=result[4],
                id_canal=result[5],
            )
        else:
            return None

    @classmethod
    def eliminar_mensaje(cls, id_mensaje):
        query = "DELETE FROM mensajes WHERE id_mensaje = %s;"
        params = (id_mensaje,)

        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False
