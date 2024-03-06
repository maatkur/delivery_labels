from dbf_repositories.users_dbf_repository import UsersDbfRepository


class DbfRepositoryManager:
    _users_dbf_repository = None
    _orders_dbf_repository = None

    @staticmethod
    def users_dbf_repository() -> UsersDbfRepository:
        if DbfRepositoryManager._users_dbf_repository is None:
            DbfRepositoryManager._users_dbf_repository = UsersDbfRepository()
        return DbfRepositoryManager._users_dbf_repository
