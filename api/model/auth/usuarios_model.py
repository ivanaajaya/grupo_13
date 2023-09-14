from ...database import DatabaseConnection
from .usuario_roles_model import UserRoleModel
# from .usuario_estado_model import UserStatusModel

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
        self.contraseña = kwargs.get('contraseña')
        self.correo_electronico = kwargs.get('correo_electronico')
        self.fecha_registro = kwargs.get('fecha_registro')
        self.estado_activo = kwargs.get('estado_activo')
        self.rol_id = kwargs.get('rol_id')
        
    # def __init__(self, id_usuario=None, alias=None, nombre=None, apellido=None, fecha_nacimiento=None, contraseña=None, correo_electronico=None, fecha_registro=None):
    #     self.id_usuario = id_usuario
    #     self.alias = alias
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.fecha_nacimiento = fecha_nacimiento
    #     self.contraseña = contraseña
    #     self.correo_electronico = correo_electronico
    #     self.fecha_registro = fecha_registro
    
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
            "contraseña": self.contraseña,
            "correo_electronico": self.correo_electronico,
            "fecha_registro": self.fecha_registro,
            "estado": self.estado_activo,
            "rol": UserRoleModel.get(UserRoleModel(rol_id = self.rol_id)).serialize()
        }
        
    @classmethod
    def is_registered(cls, user):
        """verificar si un usuario está registrado en la base de datos utilizando su nombre de alias y contraseña."""
        
        query = """SELECT user_id FROM proyecto.usuario 
        WHERE username = %(alias)s and password = %(contraseña)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params) #Los parámetros para la consulta se pasan como un diccionario (params).

        if result is not None:
            return True
        return False
    
    # @classmethod
    # def get_usuario(cls, id_usuario):
    #     query = """SELECT id_usuario, alias, nombre, apellido, fecha_nacimiento, contraseña, correo_electronico, fecha_registro 
    #     FROM proyecto.usuario WHERE id_usuario = %s;"""
    #     params = (id_usuario,)
    #     result = DatabaseConnection.fetch_one(query, params)
    #     print(type(result))
    #     if result is not None:
    #         return id_usuario(
    #             id_usuario=id_usuario[0],
    #             alias=result[1],
    #             nombre=result[2],
    #             apellido=result[3],
    #             fecha_nacimiento=result[4],
    #             contraseña=result[5],
    #             correo_electronico=result[6],
    #             fecha_registro=result[7],
    #         )
    #     else:
    #         return None
        
    @classmethod
    def get(cls, user):
        """se utiliza para buscar y obtener información detallada de un usuario en la base de datos 
        basándose en su nombre de usuario 'alias'."""
        
        query = """SELECT * FROM proyecto.usuario 
        WHERE alias = %(alias)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:#
            return cls(
                id_usuario=result[0],
                alias=result[1],
                nombre=result[1],
                apellido=result[2],
                fecha_nacimiento=result[3],
                contraseña=result[4],
                correo_electronico=result[5],
                fecha_registro=result[6],
                estado_activo=result[7],
                rol_id=result[8]
            )
        return None
        
# Registrar un usuario
    @classmethod
    def create_usuario(cls, usuario):
        
        #primero tendria que Validar que el Alias del usuario no esté en uso
        
        query = """INSERT INTO proyecto.usuario  (alias, nombre, apellido, fecha_nacimiento, contraseña, correo_electronico, fecha_registro, estado_activo, rol_id) 
        VALUES (%(alias)s, %(nombre)s, %(apellido)s, %(fecha_nacimiento)s, %(contraseña)s, %(correo_electronico)s, %(fecha_registro)s, %(estado_activo)s, %(rol_id)s);"""
        
        # params = {
        # "alias": usuario.alias,
        # "nombre": usuario.nombre,
        # "apellido": usuario.apellido,
        # "fecha_nacimiento": usuario.fecha_nacimiento,
        # "contraseña": usuario.contraseña,
        # "correo_electronico": usuario.correo_electronico,
        # "fecha_registro": usuario.fecha_registro,
        # "estado_id": usuario.estado_id,
        # "rol_id": usuario.rol_id
        # }
        params = usuario.__dict__
        
        # Ejecuta la consulta de creacion
        result = DatabaseConnection.execute_query(query, params=params)

        if result:
            return True
        else:
            return False
        
# Modifica usuario 
    @classmethod
    def update_usuario(cls, usuario):
        """Modifica un usuario existente en la base de datos."""
        
        #primero tendria que Validar que el Alias del usuario no esté en uso, PARA EL MANEJO DE ERROR
        
        query = """UPDATE proyecto.usuario SET nombre = %(nombre)s, apellido = %(apellido)s, fecha_nacimiento = %(fecha_nacimiento)s, contraseña = %(contraseña)s, correo_electronico = %(correo_electronico)s, fecha_registro = %(fecha_registro)s, estado_activo = %(estado_activo)s, rol_id = %(rol_id)s  
        WHERE alias = %(alias)s"""
        params=usuario.__dict__
        # Ejecuta la consulta de actualizacion
        result = DatabaseConnection.execute_query(query, params=params)

        if result:
            return True
        else:
            return False

#elimina usuario      
    @classmethod
    def delete_usuario(cls, id_usuario):
        """Elimina un usuario existente en la base de datos."""
        
        #primero tendria que Validar que el usuario exista, PARA EL MANEJO DE ERROR
        
        query = "DELETE FROM proyecto.usuario WHERE id_usuario = %s"
        params = (id_usuario,)

        # Ejecuta la consulta de eliminación
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False
