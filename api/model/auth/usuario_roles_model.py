from ...database import DatabaseConnection
class UserRoleModel:

    def __init__(self, **kwargs):
        self.id_rol = kwargs.get('id_rol')
        self.nombre_rol = kwargs.get('nombre_rol')
        self.permisos = kwargs.get('permisos')

    def serialize(self):
        return {
            "id_rol": self.id_rol,
            "nombre_rol": self.nombre_rol,
            "permisos": self.permisos,
        }
    
    @classmethod
    def get(cls, rol):
        query = """SELECT id_rol, nombre_rol, permisos FROM proyecto_db.roles WHERE id_rol = %(id_rol)s"""
        params = rol.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                id_rol = result[0],
                nombre_rol = result[1],
                permisos = result[2]
            )
        return None