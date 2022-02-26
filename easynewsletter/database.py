import sqlite3

from subscriber import Subscriber


class Database:
    def __init__(
        self, database_name: str = "easynewsletter.db", table_name: str = "Subscribers"
    ):
        self.database_name = database_name
        self.table_name = table_name
        self.conn = None
        self.cursor = None

    def __repr__(self) -> str:
        return f"<Database(database_name={self.database_name}, table_name={self.table_name})>"

    def __enter__(self):
        if self.database_name:
            self._open(self.database_name)

        self._create_table(self.table_name)

        return self

    def __exit__(self, *args, **kwargs) -> None:
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def _open(self, database_name: str) -> None:
        try:
            self.conn = sqlite3.connect(database_name)
            self.cursor = self.conn.cursor()
        except Exception as E:
            raise E

    def _create_table(self, table_name: str) -> None:
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name}"
            "(email TEXT, active INTEGER, id TEXT UNIQUE, created TEXT)"
        )

    def insert(self, subscribers: list) -> None:
        self.cursor.executemany(
            f"INSERT OR IGNORE INTO {self.table_name} VALUES (?, ?, ?, ?)",
            subscribers,
        )

    def delete(self, subscribers: list[Subscriber]) -> None:
        for s in subscribers:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (s.id,))

    def update(self, row_where: tuple, row_set: tuple) -> None:
        self.cursor.execute(
            f"UPDATE {self.table_name} SET {row_set[0]}=? WHERE {row_where[0]}=?",
            (row_set[1], row_where[1]),
        )

    def get(self, columns: str, limit: int = None) -> list:
        self.cursor.execute(f"SELECT {columns} FROM {self.table_name}")
        rows = self.cursor.fetchall()

        return rows[len(rows) - limit if limit else 0 :]

    def get_all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")

        return self.cursor.fetchall()
