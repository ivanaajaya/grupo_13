from ...database import DatabaseConnection

class UserStatusModel:

    def __init__(self, **kwargs):
        self.estado_id = kwargs.get('estado_id')
        self.estado_nombre = kwargs.get('estado_nombre')
    
    def serialize(self):
        return {
            "estado_id": self.estado_id,
            "estado_nombre": self.estado_nombre
        }

    @classmethod
    def get(cls, status):
        query = """SELECT estado_id, estado_nombre FROM proyecto.usuario_estado WHERE estado_id = %(estado_id)s"""
        params = status.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserStatusModel(
                estado_id = result[0],
                estado_nombre = result[1]
            )
        return None