from ...database import DatabaseConnection

# from passlib.hash import sha256_crypt

class Usuario:

    def __init__(self, **kwargs):
        """COnstructor de la clase Usuario. Recibe un conjunto de argumentos con nombre (**kwargs), 
        puede tomar múltiples argumentos clave-valor para inicializar los atributos de la clase.
        A continuación, se inicializan varios atributos de la clase a partir de los valores proporcionados en los kwargs.
        """
        self.id_usuario = kwargs.get('id_usuario')
        self.alias = kwargs.get('alias')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
        self.password = kwargs.get('password')
        self.correo_electronico = kwargs.get('correo_electronico')
        self.fecha_registro = kwargs.get('fecha_registro')
        self.estado_activo = kwargs.get('estado_activo', True)
        self.imagen = kwargs.get('imagen', None)

        
    def serialize(self):
        """Convierte la instancia de la clase en un diccionario.
        Al serializar un objeto Python a JSON, se convierte en una cadena JSON 
        que luego se puede enviar a través de una solicitud HTTP"""

        # para obtener y serializar información relacionada con el estado y el rol del usuario

        return {
            "id_usuario": self.id_usuario,
            "alias": self.alias,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_nacimiento": self.fecha_nacimiento,
            "password": self.password,
            "correo_electronico": self.correo_electronico,
            "fecha_registro": self.fecha_registro,
            "estado_activo": self.estado_activo,
            "imagen": self.imagen,
        }

    @classmethod
    def is_registered(cls, user):
        """verificar si un usuario está registrado en la base de datos utilizando su nombre de alias y contraseña."""

        query = """SELECT id_usuario FROM proyecto_db.Usuarios 
        WHERE alias = %(alias)s and password = %(password)s"""
        params = user.__dict__
        # Los parámetros para la consulta se pasan como un diccionario (params).
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def is_alias_in_use(cls, alias):
        """Verificar si un alias ya está en uso en la base de datos."""

        query = "SELECT id_usuario FROM proyecto_db.Usuarios WHERE alias = %(alias)s"
        params = {'alias': alias}
        
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def is_email_in_use(cls, correo_electronico):
        """Verificar si un correo electrónico ya está en uso en la base de datos."""

        query = "SELECT id_usuario FROM proyecto_db.Usuarios WHERE correo_electronico = %(correo_electronico)s"
        params = {'correo_electronico': correo_electronico}
        
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False

#iniciar sesion
    @classmethod
    def get(cls, user):
        """se utiliza para buscar y obtener información detallada de un usuario en la base de datos 
        basándose en su nombre de usuario 'alias'."""

        query = """SELECT * FROM proyecto_db.Usuarios WHERE alias = %(alias)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario=result[0],
                alias=result[1],
                nombre=result[2],
                apellido=result[3],
                fecha_nacimiento=result[4],
                password=result[5],
                correo_electronico=result[6],
                fecha_registro=result[7],
                estado_activo=result[8],
                imagen=result[9]
            )
        return None #usuario no encontrado
# ,
#                 id_rol=result[10]
# Registrar un usuario
    @classmethod
    def create_usuario(cls, usuario):
        """ insertar un nuevo usuario en la base de datos"""
        # primero tendria que Validar que el Alias del usuario no esté en uso

        query = """INSERT INTO proyecto_db.usuarios  (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, imagen) 
        VALUES (%(alias)s, %(nombre)s, %(apellido)s, %(fecha_nacimiento)s, %(password)s, %(correo_electronico)s, %(estado_activo)s, %(imagen)s);"""

        params = usuario.__dict__

        # Ejecuta la consulta de creacion
        result = DatabaseConnection.execute_query(query, params=params)

        if result:
            return True
        else:
            return False
# , id_rol    , %(id_rol)s
    
# Verificar la contraseña actual del usuario
    @classmethod
    def check_current_password(cls, alias, Contraseña_actual):
        """Verifica que la contraseña actual ingresada coincida con la contraseña almacenada en la base de datos."""

        query = """
        SELECT password FROM proyecto_db.usuarios
        WHERE alias = %(alias)s
        """

        params = {'alias': alias}

        # Obtiene la contraseña almacenada en la base de datos
        contraseña_almacenada = DatabaseConnection.fetch_one(query, params=params)
        # print("CONTRASEÑAAA", contraseña_almacenada)
        # print("contrasseña actual", Contraseña_actual)
        if contraseña_almacenada is not None and contraseña_almacenada[0] == Contraseña_actual:
            # print("si")
            return True
        else:
            # print("no")
            return False
        

# Modifica usuario
    @classmethod
    def update_usuario(cls, usuario):
        """Modifica un usuario existente en la base de datos."""

        query = """UPDATE proyecto_db.Usuarios SET
                alias = %(alias)s,
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                fecha_nacimiento = %(fecha_nacimiento)s,
                password = %(password)s,
                correo_electronico = %(correo_electronico)s,
                estado_activo = %(estado_activo)s,
                imagen = %(imagen)s
                WHERE id_usuario = %(id_usuario)s"""

        params = usuario.__dict__
        # Ejecuta la consulta de actualización
        result = DatabaseConnection.execute_query(query, params=params)

        if result:
            return True
        else:
            return False


# # elimina usuario
#     @classmethod
#     def delete_usuario(cls, id_usuario):
#         """Elimina un usuario existente en la base de datos."""

#         # primero tendria que Validar que el usuario exista, PARA EL MANEJO DE ERROR
#         query = "DELETE FROM proyecto_db.usuarios WHERE id_usuario = %s"
#         params = (id_usuario,)

#         # Ejecuta la consulta de eliminación
#         result = DatabaseConnection.execute_query(query, params)

#         if result:
#             return True
#         else:
#             return False
    
# Actualizar contraseña por alias
    @classmethod
    def update_password(cls, alias, new_password):
        """Actualiza la contraseña de un usuario en la base de datos por alias."""

        query = """
        UPDATE proyecto_db.usuarios
        SET password = %(new_password)s
        WHERE alias = %(alias)s
        """

        params = {'alias': alias, 'new_password': new_password}

        # Ejecuta la consulta de actualización de contraseña
        result = DatabaseConnection.execute_query(query, params=params)

        return result  # Devuelve el resultado de la actualización (True o False)

