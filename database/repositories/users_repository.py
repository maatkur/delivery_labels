from database.repositories.repository_config import RepositoryConfig


class UsersRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "users"
        super().__init__(self.table_name)

    def get_user_credential(self, user_code) -> list or None:

        command = f"""SELECT * FROM users WHERE code = {user_code}"""
        result = self.search_and_fetch(command)

        if result:
            (
                code,
                name,
                password,
                store,
            ) = result[0]
            return {
                "code": code,
                "name": name,
                "password": password,
                "store": store,
            }
        else:
            return

    def update_users(self, user) -> None:
        command = """
            INSERT OR REPLACE INTO users (code, name, password, store)
            VALUES (?, ?, ?, ?);
        """

        values = list(user.values())

        self.execute_and_commit(command, values)

