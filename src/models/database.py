from PySide6.QtSql import QSqlDatabase, QSqlQuery
from config import Database as cfg
from models.products import Product
from models.projects import Project
import sys
from traceback import print_exc


class Database(QSqlDatabase):
    def __init__(self):
        super().__init__()
        self.connection = self.addDatabase("QSQLITE")
        self.connection.setDatabaseName(cfg.name)
        try:
            self.connection.open()
            self.create_initial_tables()

        except Exception as e:
            print_exc(e)
            sys.exit(1)

    def create_initial_tables(self) -> None:
        try:
            Project.create_table(self)
            Product.create_table(self)
            return True
        except Exception as e:
            print_exc(e)
            return False

    def execute_query(self, statement: str) -> QSqlQuery:
        result = QSqlQuery(statement)
        if result.lastError().isValid():
            raise Exception(result.lastError().text())
        return result
