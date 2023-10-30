from dbf_repositories.dbf_repository import DbfRepository


class UsersDbfRepository(DbfRepository):
    def __init__(self):
        self.file = "vendedor.dbf"
        super().__init__(self.file)
        self.users = self._load()

    def get_users(self) -> list:
        processed_users = []

        for user in self.users:
            processed_users.append(
                {
                    "code": user["CODIGO"].strip(),
                    "name": user["NOME"].strip(),
                    "password": str(user["SENHA"]),
                    "store": user["EMPRESA"]
                }
            )
        return processed_users
