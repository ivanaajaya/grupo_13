from ..database import DatabaseConnection


class Servidor:
    def __init__(self, id_servidor=None, nombre_servidor=None, fecha_creacion=None, descripcion=None, id_usuario=None):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.id_usuario = id_usuario

    @classmethod
    def get_servidor(cls, id_servidor):
        # Este método recupera información sobre un servidor de la base de datos
        # basado en su ID de servidor.
        query = "SELECT id_servidor, nombre_servidor, fecha_creacion, descripcion, id_usuario FROM proyecto.usuarios WHERE id_servidor = %s;"
        params = (id_servidor,)
        result = DatabaseConnection.fetch_one(query, params)
        print(type(result))
        if result is not None:
            # Si se encontró un servidor con el ID proporcionado, se crea una instancia
            # de la clase Servidor con los datos recuperados y se devuelve.
            return cls(
                id_servidor=result[0],
                nombre_servidor=result[1],
                fecha_creacion=result[2],
                descripcion=result[3],
                id_usuario=result[4],
            )
        else:
            # Si no se encuentra ningún servidor, se devuelve None.
            return None

    @classmethod
    def create_servidor(cls, servidor):
        # Este método crea un nuevo servidor en la base de datos.
        query = "INSERT INTO proyecto.servidor (id_servidor, nombre_servidor, fecha_creacion, descripcion) VALUES (%s, %s, %s, %s);"
        params = (servidor.id_servidor, servidor.nombre_servidor,
                  servidor.fecha_creacion, servidor.descripcion)

        try:
            # Intenta ejecutar la consulta de inserción en la base de datos.
            # Si tiene éxito, devuelve un mensaje de éxito; de lo contrario, devuelve un mensaje de error.
            result = DatabaseConnection.execute_query(query, params)
            if result:
                return "El servidor se ha registrado correctamente."
            else:
                return "Hubo un problema al registrar el servidor."
        except Exception as e:
            # En caso de excepción, se captura y se devuelve un mensaje de error detallado.
            return f"Error al registrar el servidor: {str(e)}"

    @classmethod
    def delete_servidor(cls, id_servidor):
        # Este método elimina un servidor de la base de datos basado en su ID de servidor.
        query = "DELETE FROM proyecto.servidor WHERE id_servidor = %s;"
        params = (id_servidor,)

        try:
            # Intenta ejecutar la consulta de eliminación en la base de datos.
            # Si tiene éxito, devuelve un mensaje de éxito; de lo contrario, devuelve un mensaje de error.
            result = DatabaseConnection.execute_query(query, params)
            if result:
                return "El servidor se ha eliminado correctamente."
            else:
                return "No se encontró el servidor para eliminar."
        except Exception as e:
            # En caso de excepción, se captura y se devuelve un mensaje de error detallado.
            return f"Error al eliminar el servidor: {str(e)}"
