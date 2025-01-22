from PySide6.QtSql import QSqlDatabase, QSqlQuery
from config import Database as cfg
from models.products import ProductModel
from models.projects import ProjectModel
import sys
from traceback import print_exception


class Database(QSqlDatabase):
    def __init__(self):
        super().__init__()
        self.connection = self.addDatabase("QSQLITE")
        self.connection.setDatabaseName(cfg.name)
        try:
            self.connection.open()
            self.create_initial_tables()

        except Exception as e:
            print_exception(e)
            sys.exit(1)

    def create_initial_tables(self) -> None:
        try:
            ProjectModel.create_table(self)
            ProductModel.create_table(self)
            return True
        except Exception as e:
            print_exception(e)
            return False

    def execute_query(self, statement: str) -> QSqlQuery:
        result = QSqlQuery(statement)
        if result.lastError().isValid():
            raise Exception(result.lastError())
        return result
