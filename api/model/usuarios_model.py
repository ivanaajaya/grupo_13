from ..database import DatabaseConnection

class Usuario: 
    
    def __init__(self, id_usuario=None, alias=None, nombre=None, apellido=None, fecha_nacimiento=None, contraseña=None, correo_electronico=None, fecha_registro=None):
        self.id_usuario = id_usuario
        self.alias = alias
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña
        self.correo_electronico = correo_electronico
        self.fecha_registro = fecha_registro
        
    @classmethod
    def get_usuario(cls, id_usuario):
        query = "SELECT id_usuario, alias, nombre, apellido, fecha_nacimiento, contraseña, correo_electronico, fecha_registro FROM proyecto.usuarios WHERE id_usuario = %s;"
        params = (id_usuario,)
        result = DatabaseConnection.fetch_one(query, params)
        print(type(result))
        if result is not None:
            return id_usuario(
                id_usuario=id_usuario,
                alias=result[0],
                nombre=result[1],
                apellido=result[2],
                fecha_nacimiento=result[3],
                contraseña=result[4],
                correo_electronico=result[5],
                fecha_registro=result[6],
            )
        else:
            return None
        
# Registrar un usuario
    @classmethod
    def create_usuario(cls, usuario):
        query = "INSERT INTO proyecto.usuario (id_usuario, alias, nombre, apellido, fecha_nacimiento, contraseña, correo_electronico, fecha_registro) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        params = (usuario.id_usuario, usuario.alias, usuario.nombre, usuario.apellido, 
                  usuario.fecha_nacimiento, usuario.contraseña, usuario.correo_electronico, usuario.fecha_registro)
        # Ejecuta la consulta de creacion
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False
        
# Modifica usuario 
    @classmethod
    def update_usuario(cls, usuario):
        query = "UPDATE proyecto.usuario SET alias = %s, nombre = %s, fecha_nacimiento = %s, contraseña = %s, correo_electronico = %s WHERE id_usuario = %s"
        params = (usuario.alias, usuario.nombre, usuario.fecha_nacimiento, usuario.contraseña, usuario.correo_electronico)
        # Ejecuta la consulta de actualizacion
        params = (
            usuario.alias,
            usuario.nombre,
            usuario.fecha_nacimiento,
            usuario.contraseña,
            usuario.correo_electronico,
        )
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False
