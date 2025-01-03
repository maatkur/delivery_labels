from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
import pytz
from datetime import datetime
from database.base import Base


class PrinterLog(Base):
    __tablename__ = "printer_logs"

    id = Column(Integer, primary_key=True)
    order_id = Column(String(50), nullable=False)
    user_id = Column(String(50), ForeignKey("users.id"), nullable=False)
    volumes = Column(Integer, nullable=False, default=1)

    # Ajusta o fuso horário para o Brasil e usa apenas a data
    printed_at = Column(Date, default=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')).date())

    is_reprint = Column(Boolean, default=False)  # Flag para identificar reimpressão
    reprint_reason = Column(String(255), nullable=True)  # Justificativa opcional

    def __repr__(self):
        return (
            f"<PrinterLog(id={self.id}, order_id={self.order_id}, user_id={self.user_id}, "
            f"volumes={self.volumes}, printed_at={self.printed_at}, "
            f"is_reprint={self.is_reprint}, reprint_reason='{self.reprint_reason}')>"
        )
