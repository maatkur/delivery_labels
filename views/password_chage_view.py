from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from authenticator import Authenticator
from components.dialog_window.dialog_window_manager import DialogWindowManager
from database.repositories.repository_manager import RepositoryManager
from helpers import SessionHelper, WidgetHelper, EncryptHelper
from ui import ChangePasswordWindow


class ChangePasswordView(QMainWindow):

    def __init__(self) -> None:
        super(ChangePasswordView, self).__init__(parent=None)
        self.ui = ChangePasswordWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.session = SessionHelper()
        self.user = self.session.get("user")
        WidgetHelper.install_event_filters(
            self,
            [
                self.ui.current_password_input,
                self.ui.new_password_input,
                self.ui.password_confirmation_input
            ]
        )
        self.echo_mode = "hide"
        self.connect_widget_actions()

    def eventFilter(self, widget, event) -> bool:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
                self.handle_enter_key(widget)
                return True  # Indica que o evento foi tratado
        if event.type() == QtCore.QEvent.FocusIn:
            if isinstance(widget, QLineEdit):
                QtCore.QTimer.singleShot(0, lambda: widget.setCursorPosition(0))
        return super().eventFilter(widget, event)

    def handle_enter_key(self, widget) -> None:
        if widget == self.ui.current_password_input:
            self.ui.new_password_input.setFocus()
        if widget == self.ui.new_password_input:
            self.ui.password_confirmation_input.setFocus()
        if widget == self.ui.password_confirmation_input:
            if self.ui.save_button.isEnabled():
                self.change_password()

    def connect_widget_actions(self) -> None:
        self.ui.save_button.clicked.connect(self.change_password)
        self.ui.echo_mode_button.clicked.connect(self.handle_echo_mode_button)
        self.ui.current_password_input.textChanged.connect(self.manage_save_button)
        self.ui.new_password_input.textChanged.connect(self.manage_save_button)
        self.ui.password_confirmation_input.textChanged.connect(self.manage_save_button)

    def manage_password_mask(self) -> None:
        widgets = [
            self.ui.current_password_input,
            self.ui.new_password_input,
            self.ui.password_confirmation_input
        ]

        for widget in widgets:
            if self.echo_mode == "show":
                widget.setEchoMode(QLineEdit.Normal)
            else:
                widget.setEchoMode(QLineEdit.Password)

    def toggle_echo_mode(self) -> None:
        """Alterna o estado da máscara entre 'show' e 'hide'."""
        self.echo_mode = "show" if self.echo_mode == "hide" else "hide"

    def handle_echo_mode_button(self) -> None:
        """Alterna o estado da máscara e aplica a nova configuração."""
        self.toggle_echo_mode()
        self.manage_password_mask()
        self.manage_echo_mode_button_icon()

    def manage_echo_mode_button_icon(self) -> None:
        """Altera o ícone do botão de acordo com o estado da máscara."""
        icon_path = ":/newPrefix/show.ico" if self.echo_mode == "hide" else ":/newPrefix/hidden.ico"
        self.ui.echo_mode_button.setIcon(QIcon(icon_path))

    def check_passwords(self) -> bool:
        """Verifica se as senhas são iguais."""
        incomming_password = self.ui.new_password_input.text().encode('utf-8')

        status, credentials = Authenticator.authenticate(
            {
                "user_id": self.user["user_id"],
                "password": self.ui.current_password_input.text()
            }
        )

        if status.get("status") == "error":
            return False
        else:
            return True

    def check_new_password(self) -> bool:
        """Verifica se a nova senha é válida."""
        new_password = self.ui.new_password_input.text()
        password_confirmation = self.ui.password_confirmation_input.text()

        if new_password != password_confirmation:
            return False
        else:
            return True

    def change_password(self) -> None:
        """Altera a senha do usuário."""
        if not self.check_passwords():
            DialogWindowManager.dialog().error("Senha atual incorreta.")
            self.clear_fields()
            return

        if not self.check_new_password():
            DialogWindowManager.dialog().error("As senhas não coincidem.")
            self.clear_fields()
            return

        if not self.compare_old_and_new_password():
            DialogWindowManager.dialog().error("A nova senha deve ser diferente da atual.")
            self.clear_fields()
            return

        new_password = self.ui.new_password_input.text()
        RepositoryManager.users_repository().update_user(
            {
                "id": self.user["user_id"],
                "password": EncryptHelper.encrypt_password(new_password)
            }
        )
        DialogWindowManager.dialog().success("Senha alterada com sucesso.")
        self.close()

    def clear_fields(self) -> None:
        widgets = [
            self.ui.current_password_input,
            self.ui.new_password_input,
            self.ui.password_confirmation_input
        ]
        WidgetHelper.clear_widget(widgets)

        self.ui.current_password_input.setFocus()

    def manage_save_button(self) -> None:
        fields_filled = all(
            [
                len(self.ui.current_password_input.text()) > 0,
                len(self.ui.new_password_input.text()) > 0,
                len(self.ui.password_confirmation_input.text()) > 0
            ]
        )

        if fields_filled:
            WidgetHelper.enable_widget(self.ui.save_button)
        else:
            WidgetHelper.disable_widget(self.ui.save_button)

    def compare_old_and_new_password(self) -> bool:
        """Verifica se a nova senha é diferente da antiga."""
        new_password = self.ui.new_password_input.text()
        old_password = self.ui.current_password_input.text()
        return new_password != old_password


if __name__ == "__main__":
    app = QApplication()
    window = ChangePasswordView()
    window.show()
    app.exec()
