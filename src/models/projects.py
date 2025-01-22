from traceback import print_exception
from .products import ProductModel
from config import Project


class ProjectModel:
    db: object
    name: str
    total: float
    template: str
    project_id: int | None = None

    def __init__(
        self,
        db: object,
        name: str = "",
        total: float = 0.0,
        template: str = Project.default_template,
        project_id: int | None = None,
    ) -> None:
        self.db = db
        self.name = name
        self.total = total
        self.template = template
        self.project_id = self.insert() if not project_id else project_id

    @classmethod
    def create_table(cls, db) -> bool:
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
            print_exception(e)
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
                return ProjectModel(db, project_id=query.value(0), name=query.value(1))
            return None
        except Exception as e:
            print_exception(e)
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
                    ProjectModel(
                        db,
                        project_id=query.value(0),
                        name=query.value(1),
                        total=query.value(2),
                        template=query.value(3),
                    )
                )
            return projects
        except Exception as e:
            print_exception(e)
            return []

    def insert(self) -> int | None:
        try:
            statement = f"""
            INSERT INTO projects (name, total, template)
            VALUES ('{self.name}', {self.total}, '{self.template}')
            """
            result = self.db.execute_query(statement)
            self.project_id = result.lastInsertId()
            return result.lastInsertId()
        except Exception as e:
            print_exception(e)
            return None

    def update(self) -> bool:
        print("ACTUALIZANDO")
        try:
            statement = f"""
            UPDATE projects
            SET name = '{self.name}',
            total = {self.total},
            template = '{self.template}'
            WHERE id = {self.project_id}
            """
            self.db.execute_query(statement)
            return True
        except Exception as e:
            print_exception(e)
            return False

    def delete(self) -> bool:
        try:
            ProductModel.delete_products(self.db, self.project_id)
            statement = f"""
            DELETE FROM projects
            WHERE id = {self.project_id}
            """
            self.db.execute_query(statement)
            return True
        except Exception as e:
            print_exception(e)
            return False
