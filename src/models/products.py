class Products:
    def __init__(self, pid: int = None, name: str = "", price: float = 0.0):
        self.pid = pid
        self.name = name
        self.price = price

    def __dict__(self):
        return {"id": self.id, "name": self.name, "price": self.price}

    @classmethod
    def create_table(self, db) -> bool:
        try:
            statement = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get_products(self, db) -> list:
        try:
            statement = """
            SELECT * FROM products
            """
            query = db.execute_query(statement)
            products = []
            while query.next():
                products.append(
                    Products(
                        pid=query.value(0),
                        name=query.value(1),
                        price=query.value(2),
                    )
                )
            return products
        except Exception as e:
            print(e)
            return []

    @classmethod
    def insert_product(self, db, name: str, price: float) -> int | None:
        try:
            statement = f"""
            INSERT INTO products (name, price)
            VALUES ('{name}', {price})
            """
            result = db.execute_query(statement)
            return result.lastInsertId()
        except Exception as e:
            print(e)
            return None

    @classmethod
    def update_product(self, db, name: str, price: float, id: int) -> bool:
        try:
            statement = f"""
            UPDATE products
            SET name = '{name}', price = {price}
            WHERE id = {id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def delete_product(self, db, id: int) -> bool:
        try:
            statement = f"""
            DELETE FROM products
            WHERE id = {id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False
