from ...database import DatabaseConnection

class UserStatusModel:

    def __init__(self, **kwargs):
        self.id_estado = kwargs.get('id_estado')
        self.nombre_estado = kwargs.get('nombre_estado')
    
    def serialize(self):
        return {
            "id_estado": self.id_estado,
            "nombre_estado": self.nombre_estado
        }

    @classmethod
    def get(cls, status):
        query = """SELECT id_estado, nombre_estado FROM proyecto.estado_usuario WHERE id_estado = %(id_estado)s"""
        params = status.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserStatusModel(
                id_estado = result[0],
                nombre_estado = result[1]
            )
        return None