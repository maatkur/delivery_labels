from database.repositories.repository_config import RepositoryConfig


class OrdersRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "orders"
        super().__init__(self.table_name)

    def get_order(self, order_number) -> dict:
        options = {"SELECT": "*",
                   "query": {
                       "order_number": order_number
                   }}

        order_data = self.get_all(options)

        if order_data:
            (
                order_number,
                customer,
                store
            ) = order_data[0]

            return {
                "order_number": order_number,
                "customer": customer,
                "store": store
            }
