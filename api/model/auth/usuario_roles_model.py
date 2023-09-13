from ...database import DatabaseConnection

# class Rol: 
#     def __init__(self, id_rol=None, nombre_rol=None, permisos=None, id_usuario=None):
#         self.id_rol = id_rol
#         self.nombre_rol = nombre_rol
#         self.permisos = permisos
#         self.id_usuario = id_usuario

class UserRoleModel:

    def __init__(self, **kwargs):
        self.rol_id = kwargs.get('rol_id')
        self.rol_nombre = kwargs.get('rol_nombre')

    def serialize(self):
        return {
            "rol_id": self.rol_id,
            "rol_nombre": self.rol_nombre
        }
    
    @classmethod
    def get(cls, rol):
        query = """SELECT rol_id, rol_nombre FROM proyecto.ususario_roles WHERE rol_id = %(rol_id)s"""
        params = rol.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                rol_id = result[0],
                rol_nombre = result[1]
            )
        return None