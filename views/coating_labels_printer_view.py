from PySide6.QtWidgets import *

from ui import CoatingLabelsPrinterWindow


class CoatingLabelsPrinterView(QMainWindow):

    def __init__(self) -> None:
        super(CoatingLabelsPrinterView, self).__init__(parent=None)
        self.ui = CoatingLabelsPrinterWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication()
    window = CoatingLabelsPrinterView()
    window.show()
    app.exec()
