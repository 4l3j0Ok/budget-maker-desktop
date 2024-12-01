from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from config import Database as cfg
from models.products import Products
from models.projects import Projects
import sys
import traceback


class Database(QSqlDatabase):
    def __init__(self):
        super().__init__()
        self.connection = self.addDatabase("QSQLITE")
        self.connection.setDatabaseName(cfg.name)
        try:
            self.connection.open()
            self.create_initial_tables()

        except Exception as e:
            print(e)
            sys.exit(1)

    def create_initial_tables(self) -> None:
        try:
            Projects.create_table(self)
            Products.create_table(self)
            return True
        except Exception as e:
            print(e)
            return False

    def execute_query(self, statement: str) -> bool:
        try:
            query = QSqlQuery()
            if not query.exec(statement):
                raise Exception(query.lastError().text())
            return True
        except Exception as e:
            print(e)
            traceback.print_exc()
            return False
