from database.config import RepositoryConfig


class PermissionsRepository(RepositoryConfig):

    def __init__(self):
        super().__init__(table_name="permissions")
