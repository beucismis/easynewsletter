import sqlite3
import datetime


class Database:
    def __init__(
        self, database_name: str = "newsletter.db", table_name: str = "Subscribers"
    ):
        self.database_name = database_name
        self.table_name = table_name
        self.conn = None
        self.cursor = None

        if database_name:
            self._open(database_name)

        self._create_table()

    def __repr__(self) -> str:
        return f"<Database(database_name={self.database_name}, table_name={self.table_name})>"

    def __enter__(self):
        return self

    def __exit__(self) -> None:
        self._close()

    def _open(self, database_name: str) -> None:
        try:
            self.conn = sqlite3.connect(database_name)
            self.cursor = self.conn.cursor()
        except Exception as E:
            raise E

    def _close(self) -> None:
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def _create_table(self) -> None:
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name}"
            "(email TEXT, status INTEGER, id TEXT UNIQUE, created TIMESTAMP)"
        )
        self.conn.commit()

    def insert(
        self, email: str, status: int, id: str, created: datetime.datetime
    ) -> None:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} VALUES (?, ?, ?, ?)",
            (email, status, id, created),
        )

    def update(self, row_where: set, row_set: set) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} SET {row_set[0]}=? WHERE {row_where[0]}=?",
            (row_set[1], row_where[1]),
        )

    def delete(self, row: str, value) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE {row}=?", (value,))

    def get(self, columns: str, limit: int = None) -> set:
        self.cursor.execute(f"SELECT {columns} FROM {self.table_name}")
        rows = self.cursor.fetchall()

        return rows[len(rows) - limit if limit else 0 :]

    def get_last(self, columns: str) -> set:
        return self.get(columns, limit=1)[0]
