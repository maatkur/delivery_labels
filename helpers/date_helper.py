import datetime
from PySide6.QtCore import QDate


class DateHelper:

    @staticmethod
    def get_current_date():
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%d/%m/%Y")
        return formatted_date

    @staticmethod
    def to_qdate(date: str):
        return QDate.fromString(date, "dd/MM/yyyy")

    @staticmethod
    def to_sql_date(date: str):
        return datetime.datetime.strptime(date, "%d/%m/%Y").date()
