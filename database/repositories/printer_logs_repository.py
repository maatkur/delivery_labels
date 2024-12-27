from typing import Optional

from database.config import RepositoryConfig
from database.models import PrinterLog  # Importe o modelo User


class PrinterLogsRepository(RepositoryConfig):

    def __init__(self):
        super().__init__(table_name="printer_logs")

    def create_printer_log(self, printer_log_data: dict) -> None:
        # Cria uma instância do modelo PrinterLog com os parâmetros
        new_printer_log = PrinterLog(
            order_id=printer_log_data["order_id"],
            user_id=printer_log_data["user_id"],
            volumes=printer_log_data["volumes"],
            is_reprint=printer_log_data["is_reprint"],
            reprint_reason=printer_log_data["reprint_reason"]
        )

        # Agora adiciona essa instância ao banco
        self.execute_and_commit(new_printer_log)

    def verify_reprint(self, order_id: str) -> Optional[bool]:
        """
        Verifica se a ordem já foi impressa.
        """
        result = self.search(PrinterLog, {"order_id": order_id})

        if result:
            return True
        return False
