from .products import Product


class Project:
    project_id: int | None = None
    name: str
    total: float
    template: str | None = None

    def __init__(
        self,
        name: str,
        total: float,
        template: str,
        project_id: int | None = None,
    ) -> None:
        self.name = name
        self.total = total
        self.project_id = project_id
        self.template = template

    @classmethod
    def create_table(self, db) -> bool:
        try:
            statement = """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                total REAL NOT NULL,
                template TEXT NOT NULL
            )
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get(self, db, project_id: int):
        try:
            statement = f"""
            SELECT * FROM projects
            WHERE id = {project_id}
            """
            query = db.execute_query(statement)
            if query.next():
                return Project(project_id=query.value(0), name=query.value(1))
            return None
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_all(self, db) -> list:
        try:
            statement = """
            SELECT * FROM projects
            """
            query = db.execute_query(statement)
            projects = []
            while query.next():
                projects.append(
                    Project(
                        project_id=query.value(0),
                        name=query.value(1),
                        total=query.value(2),
                        template=query.value(3),
                    )
                )
            return projects
        except Exception as e:
            print(e)
            return []

    def insert(self, db) -> int | None:
        try:
            statement = f"""
            INSERT INTO projects (name, total, template)
            VALUES ('{self.name}', {self.total}, '{self.template}')
            """
            result = db.execute_query(statement)
            self.project_id = result.lastInsertId()
            return result.lastInsertId()
        except Exception as e:
            print(e)
            return None

    def update(self, db) -> bool:
        try:
            statement = f"""
            UPDATE projects
            SET name = '{self.name}',
            total = {self.total},
            template = '{self.template}'
            WHERE id = {self.project_id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, db) -> bool:
        try:
            Product.delete_products(db, self.project_id)
            statement = f"""
            DELETE FROM projects
            WHERE id = {self.project_id}
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False
