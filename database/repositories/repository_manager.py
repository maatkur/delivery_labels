from .users_repository import UsersRepository
from .users_permission_repository import UsersPermissionsRepository
from .printed_labels_repository import PrintedLabelsRepository


class RepositoryManager:
    _users_repository = None
    _orders_repository = None
    _users_permission_repository = None
    _printed_labels_repository = None

    @staticmethod
    def users_repository() -> UsersRepository:
        if RepositoryManager._users_repository is None:
            RepositoryManager._users_repository = UsersRepository()
        return RepositoryManager._users_repository

    @staticmethod
    def users_permissions_repository() -> UsersPermissionsRepository:
        if RepositoryManager._users_permission_repository is None:
            RepositoryManager._users_permission_repository = UsersPermissionsRepository()
        return RepositoryManager._users_permission_repository

    @staticmethod
    def printed_labels_repository() -> PrintedLabelsRepository:
        if RepositoryManager._printed_labels_repository is None:
            RepositoryManager._printed_labels_repository = PrintedLabelsRepository()
        return RepositoryManager._printed_labels_repository
