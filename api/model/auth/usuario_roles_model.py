from ...database import DatabaseConnection
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
        query = """SELECT id_rol, nombre_rol, permisos FROM proyecto.roles WHERE id_rol = %(id_rol)s"""
        params = rol.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                id_rol = result[0],
                nombre_rol = result[1],
                permisos = result[1]
            )
        return None