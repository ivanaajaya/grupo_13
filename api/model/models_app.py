from ..database import DatabaseConnection

#CLASE App

class App: 
    pass
#Ejemplo:

""" class Product:
    def __init__(self, product_id=None, product_name=None, brand_id=None, category_id=None, model_year=None, list_price=None):
        self.product_id = product_id
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price

    # 2.1. Mostrar un producto
    @classmethod
    def get_product(cls, product_id):
        query = "SELECT product_name, brand_id, category_id, model_year, list_price FROM production.products WHERE product_id = %s;"
        params = (product_id,)
        result = DatabaseConnection.fetch_one(query, params)
        print(type(result))
        if result is not None:
            return Product(
                product_id=product_id,
                product_name=result[0],
                brand_id=result[1],
                category_id=result[2],
                model_year=result[3],
                list_price=result[4]
            )
        else:
            return None

    # 2.2. Mostrar lista de productos
    @classmethod
    def get_products_with_filters(cls, brand_id=None, category_id=None):
        query = "SELECT product_id, product_name, brand_id, category_id, model_year, list_price FROM production.products"

        conditions = []
        params = []

        if brand_id is not None:
            conditions.append("brand_id = %s")
            params.append(brand_id)

        if category_id is not None:
            conditions.append("category_id = %s")
            params.append(category_id)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        db = DatabaseConnection()  # Assuming DatabaseConnection is properly configured
        results = db.fetch_all(query, params)

        products = []
        for result in results:
            product = Product(
                product_id=result[0],
                product_name=result[1],
                brand_id=result[2],
                category_id=result[3],
                model_year=result[4],
                list_price=result[5]
            )
            products.append(product)

        return products

 # 2.3. Registrar un producto
    @classmethod
    def create_product(cls, product):
        query = "INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s);"
        params = (product.product_name, product.brand_id,
                  product.category_id, product.model_year, product.list_price)
        # Ejecuta la consulta de creacion
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False

    # 2.4. Modificar un producto
    @classmethod
    def update_product(cls, product_update):
        query = "UPDATE production.products SET product_name = %s WHERE product_id = %s"
        query = "UPDATE production.products SET product_name = %s, brand_id = %s, category_id = %s, model_year = %s, list_price = %s WHERE product_id = %s"
        params = (product_update.product_name, product_update.product_id)
        # Ejecuta la consulta de actualizacion
        params = (
            product_update.product_name,
            product_update.brand_id,
            product_update.category_id,
            product_update.model_year,
            product_update.list_price,
            product_update.product_id
        )
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False

    # 2.5. Eliminar un producto
    @classmethod
    def delete_product(cls, product_id):
        query = "DELETE FROM production.products WHERE product_id = %s"
        params = (product_id,)

        # Ejecuta la consulta de eliminación
        result = DatabaseConnection.execute_query(query, params)

        if result:
            return True
        else:
            return False """
