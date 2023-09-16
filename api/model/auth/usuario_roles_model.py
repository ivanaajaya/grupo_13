from ...database import DatabaseConnection
class UserRoleModel:

    def __init__(self, **kwargs):
        self.id_rol = kwargs.get('id_rol')
        self.nombre_rol = kwargs.get('nombre_rol')
        self.permisos = kwargs.get('permisos')
        self.id_usuario = kwargs.get('id_usuario')

    def serialize(self):
        return {
            "id_rol": self.id_rol,
            "nombre_rol": self.nombre_rol,
            "permisos": self.permisos,
            "id_usuario": self.id_usuario
        }
    
    @classmethod
    def get(cls, rol):
        query = """SELECT id_rol, nombre_rol, permisos, id_usuario FROM proyecto_db.roles WHERE id_rol = %(id_rol)s"""
        params = rol.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                id_rol = result[0],
                nombre_rol = result[1],
                permisos = result[2],
                id_usuario = result[3]
            )
        return None