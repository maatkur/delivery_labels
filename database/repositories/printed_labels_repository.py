from database.repositories.repository_config import RepositoryConfig


class PrintedLabelsRepository(RepositoryConfig):

    def __init__(self):
        self.table_name = "printed_labels"
        super().__init__(self.table_name)

    def check_label(self, order_number) -> bool:

        result = self.select(
            {
                "query": {"order_number": order_number}
            }
        )

        if result:
            return True
        else:
            return False
