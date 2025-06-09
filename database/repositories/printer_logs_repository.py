from typing import Optional

from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

from database.config import RepositoryConfig, get_session
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

    def verify_reprint_volumes(self, order_id: str) -> Optional[int]:
        """
        Retorna o número de volumes da última impressão de uma ordem específica.

        Args:
            order_id (str): O ID da ordem a ser verificada.

        Returns:
            Optional[int]: O número de volumes da última impressão ou None se não encontrada.
        """
        try:
            with get_session() as session:
                result = (
                    session.query(PrinterLog.volumes)
                    .filter_by(order_id=order_id)
                    .order_by(desc(PrinterLog.printed_at), desc(PrinterLog.id))
                    .first()
                )
                return result.volumes if result else None
        except SQLAlchemyError as e:
            print(f"Erro ao buscar volumes: {e}")
            return None



