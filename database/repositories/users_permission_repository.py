from database.repositories.repository_config import RepositoryConfig


class UsersPermissionsRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "users_permissions"
        super().__init__(self.table_name)

    def retrieve_user_permissions(self, user_code:str) -> dict:

        options = {"select": "admin, reprint, report_access",
                   "query": {"code": user_code}}

        user_permission = self.get_all(options)

        if user_permission:
            (
                admin,
                reprint,
                report_access,
            ) = user_permission[0]

            return {
                "admin": admin,
                "reprint": reprint,
                "report_access": report_access,
            }

    def get_all_permissions(self) -> list:

        command = """SELECT users.code, 
                            users.name, 
                            users_permissions.admin, 
                            users_permissions.reprint , 
                            users_permissions.report_access  
                    FROM users
                    INNER JOIN users_permissions on users.code = users_permissions.code"""

        result = self.search_and_fetch(command)

        return result

    def update_user_permission(self, options: dict) -> None:

        command = f"""
                    UPDATE {self.table_name}
                    SET {options["permission"]} = {options["value"]}
                    WHERE code = {options["code"]}
                    """

        self.execute_and_commit(command)

    # def get_u