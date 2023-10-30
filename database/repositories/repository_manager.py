from database.repositories import UsersRepository, OrdersRepository


class RepositoryManager:
    _users_repository = None
    _orders_repository = None

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
