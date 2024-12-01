class Projects:
    @classmethod
    def create_table(self, db) -> bool:
        try:
            statement = """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
            """
            db.execute_query(statement)
            return True
        except Exception as e:
            print(e)
            return False
