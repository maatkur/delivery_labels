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

    def search_error(self) -> None:
        title = "Ops!"
        message = "Pedido inválido!!!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def confirmation(self) -> bool:
        title = "CONFIRMAR?"
        message = "INICIAR ATUALIZAÇÃO DE USUÁRIOS?"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.message_box.setDefaultButton(QMessageBox.Cancel)
        result = self.message_box.exec()

        return result

    def start_users_update(self) -> None:
        title = "INICIANDO ATUALIZAÇÃO DE USUÁRIOS!"
        message = "CLIQUE EM 'OK' E AGUARDE A MENSAGEM DE CONCLUSÃO PARA CONTINUAR!!!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def finish_users_update(self) -> None:
        title = "Aviso!"
        message = "Atualização de usuários concluída!!!"

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
