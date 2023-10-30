from database.repositories.repository import Repository


class OrdersRepository(Repository):

    def __init__(self):
        self.table_name = "orders"
        super().__init__(self.table_name)

