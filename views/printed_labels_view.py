from PySide6.QtWidgets import *
from PySide6.QtCore import QDate
from ui import PrintedLabelsWindow
from datetime import datetime


class PrintedLabelsView(QMainWindow):
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(PrintedLabelsView, self).__init__(parent=None)
        self.ui = PrintedLabelsWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.date_entry.setDate(self.qdate)

    def load_table(self, labels: list) -> None:

        # Definir o número de linhas e colunas
        self.ui.tableWidget.setRowCount(len(labels))
        self.ui.tableWidget.setColumnCount(len(labels[0]))

        # Preencher os labels
        for row, row_data in enumerate(labels):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))

                # Defina o item da célula da tabela
                self.ui.tableWidget.setItem(row, col, item)  # Define o item na tabela


if __name__ == "__main__":
    app = QApplication()
    window = PrintedLabelsView()
    window.show()
    app.exec()

