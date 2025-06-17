from logger import logger


class PostUpdate:
    queries = []

    def run(self, db) -> str:
        self.add_comment_column_query(db)
        if not self.queries:
            logger.info("No hay queries de actualización pendientes.")
            return "No hay actualizaciones pendientes."
        for query in self.queries:
            try:
                logger.info(f"Ejecutando query de update: {query.strip()}")
                db.execute_query(query)
            except Exception as ex:
                logger.exception(ex)
                return str(ex)

    def add_comment_column_query(self, db) -> str:
        cursor = db.execute_query("PRAGMA table_info(products);")
        found = False
        while cursor.next():
            record = cursor.record()
            if record.value("name") == "comment":
                found = True
                break
        if not found:
            logger.info("Añadiendo columna 'comment' a la tabla 'products'")
            self.queries.append(
                "ALTER TABLE products ADD COLUMN comment TEXT DEFAULT ''"
            )
