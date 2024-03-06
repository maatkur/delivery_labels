from helpers.file_helper import FileHelper
from dbf_repositories.dbf_repository_manager import DbfRepositoryManager
from database.repositories.repository_manager import RepositoryManager


class OrdersUpdateHelper:

    @staticmethod
    def _get_orders_file() -> None:
        FileHelper.copy_orders_file()

    @staticmethod
    def _retrieve_orders() -> list:
        return DbfRepositoryManager.orders_dbf_repository().get_orders()

    @staticmethod
    def _update(orders: list) -> None:

        for order in orders:
            RepositoryManager.orders_repository().insert(order)

    @staticmethod
    def _delete_orders_file() -> None:
        FileHelper.delete_orders_file()

    @staticmethod
    def execute_update() -> None:

        OrdersUpdateHelper._get_orders_file()
        orders = OrdersUpdateHelper._retrieve_orders()
        OrdersUpdateHelper._update(orders)
        OrdersUpdateHelper._delete_orders_file()
