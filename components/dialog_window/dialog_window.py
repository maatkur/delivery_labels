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

