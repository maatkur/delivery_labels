from .users_repository import UsersRepository
from .users_permissions_repository import UsersPermissionsRepository
from .printer_logs_repository import PrinterLogsRepository
from .permissions_repository import PermissionsRepository


class RepositoryManager:
    _users_repository = None
    _orders_repository = None
    _users_permission_repository = None
    _printer_logs_repository = None
    _permissions_repository = None

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
    def printer_logs_repository() -> PrinterLogsRepository:
        if RepositoryManager._printer_logs_repository is None:
            RepositoryManager._printer_logs_repository = PrinterLogsRepository()
        return RepositoryManager._printer_logs_repository

    @staticmethod
    def permissions_repository() -> PermissionsRepository:
        if RepositoryManager._permissions_repository is None:
            RepositoryManager._permissions_repository = PermissionsRepository()
        return RepositoryManager._permissions_repository
