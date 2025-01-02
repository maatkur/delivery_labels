from PySide6.QtWidgets import QMessageBox


class DialogWindow:
    def __init__(self):
        self.message_box = QMessageBox()

    def login_error(self) -> None:
        title = "Ops!"
        message = "Usuário e/ou senha inválido(s)!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def error(self, message: str) -> None:
        title = "Ops!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def success(self, message: str) -> None:
        title = "Sucesso!"

        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def search_error(self) -> None:
        title = "Ops!"
        message = "Pedido inválido!!!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def already_printed(self) -> None:
        title = "Ops!"
        message = "Essa etiqueta já foi impressa!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()
