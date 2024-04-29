import os
import sqlite3

from helpers import dict_helpers


class RepositoryConfig:
    def __init__(self, table_name):
        self._database = os.getenv("DATABASE")
        self.table_name = table_name
        self._connection = None
        self._cursor = None
        if type(self) is RepositoryConfig:
            raise NotImplemented("Repository class cannot be started directly, you must use it as inheritance")

    def _connect(self) -> None:
        try:
            self._connection = sqlite3.connect(self._database)
            self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _disconnect(self) -> None:
        self._cursor.close()
        self._connection.close()

    def execute_and_commit(self, command, values=None) -> None:
        # Executa uma consulta que altera dados no banco de dados e realiza um commit.
        try:
            self._connect()
            if values:
                self._cursor.execute(command, values)
            else:
                self._cursor.execute(command)
            self._connection.commit()
            self._disconnect()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            self._connection.rollback()
            self._disconnect()
            raise

    def insert(self, data: dict) -> None:
        keys = ", ".join(data.keys())
        placeholders = ", ".join(
            ["?"] * len(data))  # Cria uma string com a mesma quantidade de placeholders que os valores

        command = f"INSERT OR REPLACE INTO {self.table_name} ({keys}) VALUES ({placeholders})"
        values = tuple(data.values())  # Cria uma tupla com os valores do dicionário

        self.execute_and_commit(command, values)

    def search_and_fetch(self, command, values=()) -> list:
        # Executa uma busca e retorna o resultado em uma lista de tuplas
        self._connect()
        self._cursor.execute(command, values)
        result = self._cursor.fetchall()
        self._disconnect()
        return result

    def select(self, options: dict) -> list:
        options = dict_helpers.dict_merge({"select": "*"}, options)
        command = f"SELECT"
        command += f" {options['select']} FROM {self.table_name} "
        if options.get('query'):
            query = dict_helpers.dict_to_query(options['query'])
            command += query

        return self.search_and_fetch(command)
