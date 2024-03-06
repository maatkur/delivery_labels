from database.repositories import UsersRepository, OrdersRepository, UsersPermissionsRepository


class RepositoryManager:
    _users_repository = None
    _orders_repository = None
    _users_permission_repository = None

    @staticmethod
    def users_repository() -> UsersRepository:
        if RepositoryManager._users_repository is None:
            RepositoryManager._users_repository = UsersRepository()
        return RepositoryManager._users_repository

    @staticmethod
    def orders_repository() -> OrdersRepository:
        if RepositoryManager._orders_repository is None:
            RepositoryManager._orders_repository = OrdersRepository()
        return RepositoryManager._orders_repository

    @staticmethod
    def users_permissions_repository() -> UsersPermissionsRepository:
        if RepositoryManager._users_permission_repository is None:
            RepositoryManager._users_permission_repository = UsersPermissionsRepository()
        return RepositoryManager._users_permission_repository
