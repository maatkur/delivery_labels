from PySide6 import QtCore
from PySide6.QtWidgets import *
from ui import LoginWindow
from views.labels_printer_view import LabelsPrinterView

from helpers import WidgetHelper, LoggedUserHelper
from components import DialogWindowManager

from authenticator.authenticator import Authenticator
from dotenv import load_dotenv

load_dotenv(r'C:\Users\mathe\PycharmProjects\delivery_labels\config\development.env')


class LabelsLoginView(QMainWindow):

    def __init__(self) -> None:
        super(LabelsLoginView, self).__init__(parent=None)
        self.ui = LoginWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        WidgetHelper.install_event_filters(self, [
            self.ui.user_entry,
            self.ui.password_entry,
            self.ui.login_button
        ])
        WidgetHelper.disable_widget(self.ui.login_button)
        self.connect_widget_actions()
        self.labels_printer_window = None

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
                self.handle_enter_key(widget)
                return True  # Indica que o evento foi tratado
        return super().eventFilter(widget, event)

    def handle_enter_key(self, widget):
        if widget == self.ui.user_entry:
            self.focusNextChild()
        elif widget == self.ui.password_entry:
            self.login()
        elif widget == self.ui.login_button:
            self.login()

    def manage_login_button(self) -> None:
        user_fields_filled = (len(self.ui.user_entry.text()) > 0) and (len(self.ui.password_entry.text()) > 0)
        if user_fields_filled:
            WidgetHelper.enable_widget(self.ui.login_button)
        else:
            WidgetHelper.disable_widget(self.ui.login_button)

    def connect_widget_actions(self) -> None:
        self.ui.user_entry.textChanged.connect(self.manage_login_button)
        self.ui.password_entry.textChanged.connect(self.manage_login_button)

    def login(self) -> None:
        user = {
            "code": self.ui.user_entry.text(),
            "password":  self.ui.password_entry.text()
        }
        authenticated_user = Authenticator.authenticate(user)

        if authenticated_user:
            LoggedUserHelper.logged_user().set_data(authenticated_user)
            if self.labels_printer_window is None:
                self.labels_printer_window = LabelsPrinterView()
                self.labels_printer_window.show()
            window.close()
        else:
            self.clear_fields()
            DialogWindowManager.dialog().login_error()

    def clear_fields(self) -> None:
        widgets = [self.ui.user_entry, self.ui.password_entry]
        WidgetHelper.clear_widget(widgets)
        self.ui.user_entry.setFocus()


if __name__ == "__main__":
    app = QApplication()
    window = LabelsLoginView()
    window.show()
    app.exec()
