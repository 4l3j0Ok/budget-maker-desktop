class ProjectProducts:
    @classmethod
    def create_table(self, db) -> bool:
        try:
            statement = """
            CREATE TABLE IF NOT EXISTS project_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                amount INTEGER NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False
