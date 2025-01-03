from typing import Optional, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

from database.models import PrinterLog
from database.repositories.repository_manager import RepositoryManager
from helpers import WidgetHelper, DateHelper
from ui import PrintedLabelsWindow


class PrintedLabelsView(QMainWindow):

    def __init__(self) -> None:
        super(PrintedLabelsView, self).__init__(parent=None)
        self.ui = PrintedLabelsWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.date_entry.setDate(DateHelper.to_qdate(DateHelper.get_current_date()))
        self.search_and_populate()
        self.ui.date_entry.dateChanged.connect(self.search_and_populate)

    def search(self) -> Optional[List[PrinterLog]]:
        """
        Busca os registros de etiquetas impressas no banco de dados.
        """
        # Obtém a data selecionada
        selected_date = DateHelper.to_sql_date(self.ui.date_entry.text())

        # Busca os registros no banco de dados
        logs = RepositoryManager.printer_logs_repository().search(PrinterLog, {"printed_at": selected_date})

        return logs

    def populate_table(self, data):
        """
        Preenche uma QTableWidget com os dados fornecidos e ajusta a tabela à tela.

        Args:
            data (list): Lista de objetos PrinterLog.
        """
        # Limpa a tabela
        WidgetHelper.clear_table(self.ui.tableWidget)

        self.ui.tableWidget.setRowCount(len(data))  # Define o número de linhas
        self.ui.tableWidget.setColumnCount(6)  # Define o número de colunas

        # Preenche as linhas da tabela
        for row_idx, log in enumerate(data):
            # Insere os valores em cada célula
            items = [
                QTableWidgetItem(str(log.order_id)),
                QTableWidgetItem(str(log.user_id)),
                QTableWidgetItem(str(log.volumes)),
                QTableWidgetItem(log.printed_at.strftime("%Y-%m-%d")),
                QTableWidgetItem("Sim" if log.is_reprint else "Não"),
                QTableWidgetItem(log.reprint_reason or "Nenhum"),
            ]

            for col_idx, item in enumerate(items):
                item.setTextAlignment(Qt.AlignCenter)  # Centraliza o conteúdo
                self.ui.tableWidget.setItem(row_idx, col_idx, item)

        # Ajusta o tamanho das colunas e linhas ao conteúdo
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

        # Configura o redimensionamento das colunas para ocupar todo o espaço disponível
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def search_and_populate(self):
        """
        Busca os registros de etiquetas impressas no banco de dados e preenche a tabela.
        """
        data = self.search()
        self.populate_table(data)


if __name__ == "__main__":
    app = QApplication()
    window = PrintedLabelsView()
    window.show()
    app.exec()

