from database.config import RepositoryConfig
from database.models import Permission


class PermissionsRepository(RepositoryConfig):

    def __init__(self):
        super().__init__(table_name="permissions")

    def create_permission(self, permission_data: dict) -> None:
        new_permission = Permission(
            description=permission_data["description"]
        )
        self.execute_and_commit(new_permission)
