import sys
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from config import Path
from models.products import ProductModel
from models.projects import ProjectModel
from logger import logger


class Database(QSqlDatabase):
    def __init__(self):
        super().__init__()
        self.connection = self.addDatabase("QSQLITE")
        self.connection.setDatabaseName(Path.database)
        try:
            self.connection.open()
            self.create_initial_tables()

        except Exception as ex:
            logger.exception(ex)
            sys.exit(1)

    def create_initial_tables(self) -> None:
        try:
            ProjectModel.create_table(self)
            ProductModel.create_table(self)
            return True
        except Exception as ex:
            logger.exception(ex)
            return False

    def execute_query(self, statement: str) -> QSqlQuery:
        result = QSqlQuery(statement)
        if result.lastError().isValid():
            raise Exception(result.lastError())
        return result
