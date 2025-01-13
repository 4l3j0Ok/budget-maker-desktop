class Product:
    name: str
    quantity: int
    cost: float
    cost_visible: bool
    project_id: int | None = None
    product_id: int | None = None

    def __init__(
        self, name: str, quantity: int, cost: float, cost_visible: bool
    ) -> None:
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.cost_visible = cost_visible

    @classmethod
    def create_table(self, db) -> bool:
        try:
            statement = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cost REAL NOT NULL,
                quantity INTEGER NOT NULL,
                cost_visible BOOLEAN NOT NULL,
                project_id INTEGER NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects(id)
            )
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get(self, db, project_id) -> list:
        try:
            statement = f"""
            SELECT * FROM products WHERE project_id = {project_id}
            """
            query = db.execute_query(statement)
            products = []
            while query.next():
                products.append(
                    Product(
                        name=query.value(1),
                        quantity=query.value(2),
                        cost=query.value(3),
                        cost_visible=query.value(4),
                    )
                )
            return products
        except Exception as e:
            print(e)
            return []

    def insert(self, db) -> int | None:
        try:
            statement = f"""
            INSERT INTO products (name, quantity, cost, cost_visible, project_id)
            VALUES ('{self.name}', {self.quantity}, {self.cost}, {self.cost_visible}, {self.project_id})
            """
            result = db.execute_query(statement)
            self.product_id = result.lastInsertId()
            return result.lastInsertId()
        except Exception as e:
            print(e)
            return None

    def update(self, db) -> bool:
        try:
            statement = f"""
            UPDATE products
            SET name = '{self.name}', quantity = {self.quantity}, cost = {self.cost}, cost_visible = {self.cost_visible}
            WHERE id = {self.product_id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, db, product_id: int) -> bool:
        try:
            statement = f"""
            DELETE FROM products
            WHERE id = {product_id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_products(self, db, project_id: int) -> bool:
        try:
            statement = f"""
            DELETE FROM products
            WHERE project_id = {project_id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False
