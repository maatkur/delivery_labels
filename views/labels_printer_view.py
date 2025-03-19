from PySide6 import QtCore
from PySide6.QtWidgets import *

from components.dialog_window.dialog_window_manager import DialogWindowManager
from database.repositories.repository_manager import RepositoryManager
from helpers import SessionHelper
from helpers import WidgetHelper
from helpers.query_helper import QueryHelper
from helpers.date_helper import DateHelper
from ui import LabelPrinterWindow
from views.labels_report_view import PrintedLabelsView
from views.users_management_view import UsersManagementView
from views.password_chage_view import ChangePasswordView
from printer.printer import Printer


class LabelsPrinterView(QMainWindow):

    def __init__(self) -> None:
        super(LabelsPrinterView, self).__init__(parent=None)
        self.ui = LabelPrinterWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.session = SessionHelper()
        self.user = self.session.get("user")
        self.users_management_window = None
        self.printed_labels_window = None
        self.change_password_window = None
        self.show_logged_user()
        self.order_data = None
        self.orders_update_window = None
        self.reprint_frame_activated = False
        self.manage_users_management_button()
        self.manage_report_button()
        self.connect_widgets_actions()
        WidgetHelper.install_event_filters(self, [
            self.ui.menu_button,
            self.ui.order_entry,
            self.ui.search_button,
            self.ui.clear_button,
            self.ui.print_button,
            self.ui.users_menu_button,
            self.ui.reports_button,
            self.ui.change_password_button,
            self.ui.increment_button,
            self.ui.decrement_button
        ]
                                           )

    def connect_widgets_actions(self) -> None:
        self.ui.customer_field.textChanged.connect(self.manage_print_button)
        self.ui.customer_field.textChanged.connect(self.manage_clear_button)
        self.ui.order_entry.textChanged.connect(self.manage_search_button)
        self.ui.users_menu_button.clicked.connect(self.handle_users_management_button)
        self.ui.reasons_combo_box.currentTextChanged.connect(self.manage_print_button)
        self.ui.print_button.clicked.connect(self.handle_print_button)
        self.ui.change_password_button.clicked.connect(self.handle_change_password_button)

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
                self.handle_enter_key(widget)
                return True  # Indica que o evento foi tratado
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            self.handle_mouse_click(widget)
        return super().eventFilter(widget, event)

    def handle_enter_key(self, widget):
        if widget == self.ui.order_entry:
            self.search_order()

    def handle_mouse_click(self, widget):
        if widget == self.ui.menu_button:
            self.manage_drawer()
        if widget == self.ui.increment_button:
            self.change_quantity_display(1)
            self.change_quantity_label()
        if widget == self.ui.decrement_button:
            self.change_quantity_display(-1)
            self.change_quantity_label()
        if widget == self.ui.clear_button:
            self.new_search()
        if widget == self.ui.search_button:
            self.search_order()
        if "MANAGE USERS" in self.user["permissions"]:
            if widget == self.ui.users_menu_button:
                self.handle_users_management_button()
        if "REPORT" in self.user["permissions"]:
            if widget == self.ui.reports_button:
                self.handle_report_button()

    def manage_drawer(self) -> None:
        drawer_closed = self.ui.drawer.width() == 0

        if drawer_closed:
            self.ui.drawer.setMinimumWidth(49)
        else:
            self.ui.drawer.setMinimumWidth(0)

    def activate_reprint_frame(self) -> None:

        self.reprint_frame_activated = True
        self.resize(600, 250)
        self.ui.reprint_frame.setMinimumHeight(38)

    def deactivate_reprint_frame(self) -> None:

        self.reprint_frame_activated = False
        self.resize(600, 200)
        self.ui.reprint_frame.setMinimumHeight(0)
        self.ui.reasons_combo_box.setCurrentText("Selecione")

    def change_quantity_display(self, value) -> None:
        volume = int(self.ui.label_quantity_display.text())

        volume += value

        if 1 <= volume <= 36:
            self.ui.label_quantity_display.setText(f"{volume}")

    def change_quantity_label(self) -> None:
        volume = int(self.ui.label_quantity_display.text())

        if volume == 1:
            self.ui.quantity_label.setText("VOLUME ÚNICO")
        if volume > 1:
            self.ui.quantity_label.setText(f"{volume} VOLUMES PARA IMPRESSÃO")

    def new_search(self) -> None:

        widgets = [
            self.ui.order_entry,
            self.ui.customer_field,
            self.ui.service_store_field,
            self.ui.label_date_field,
            self.ui.checker_field,
        ]
        WidgetHelper.clear_widget(widgets)
        self.ui.label_quantity_display.setText("1")
        self.ui.quantity_label.setText("VOLUME ÚNICO")
        self.enable_search_field()
        self.deactivate_reprint_frame()

    def search_order(self) -> None:
        order_number = self.ui.order_entry.text()

        self.order_data = QueryHelper.query_response(order_number)
        print(self.order_data)
        if self.order_data:
            self.manage_print_permissions()
        else:
            DialogWindowManager.dialog().search_error()
            self.new_search()

    def load_label_data(self) -> None:
        # TODO: Refatorar para utilizar o método de formatação de strings

        self.ui.customer_field.setText(self.order_data["nome"])
        self.ui.service_store_field.setText(
            self.order_data["loja"].replace("-", " ").replace("OBRA", "").replace("FACIL", "").replace("CD", "")
        )
        self.ui.label_date_field.setText(DateHelper.get_current_date())
        self.ui.checker_field.setText(f'{self.user["user_id"]}')

    def show_logged_user(self) -> None:

        self.ui.logged_user_label.setText(f"{self.user['user_id']}-{self.user['name']}")

    def disable_search_field(self) -> None:
        self.ui.order_entry.setDisabled(True)

    def enable_search_field(self) -> None:
        self.ui.order_entry.setDisabled(False)

    # TODO: Simplificar a lógica de desabilitar e habilitar botões
    def disable_search_button(self) -> None:
        self.ui.search_button.setDisabled(True)

    def enable_search_button(self) -> None:
        self.ui.search_button.setDisabled(False)

    def manage_search_button(self) -> None:
        order_entry_filled = len(self.ui.order_entry.text()) > 0

        if order_entry_filled:
            self.enable_search_button()
        else:
            self.disable_search_button()

    def disable_admin_widgets(self) -> None:
        widgets = [
            self.ui.users_menu_button,
            self.ui.reports_button
        ]

        WidgetHelper.disable_widget(widgets)

    def enable_admin_widgets(self) -> None:
        widgets = [
            self.ui.users_menu_button,
            self.ui.reports_button
        ]

        WidgetHelper.enable_widget(widgets)

    def manage_users_management_button(self) -> None:
        if "MANAGE USERS" in self.user["permissions"]:
            WidgetHelper.enable_widget(self.ui.users_menu_button)
        else:
            WidgetHelper.disable_widget(self.ui.users_menu_button)

    def manage_report_button(self) -> None:
        if "REPORT" in self.user["permissions"]:
            WidgetHelper.enable_widget(self.ui.reports_button)
        else:
            WidgetHelper.disable_widget(self.ui.reports_button)

    def manage_print_button(self) -> None:
        label_data_filled = len(self.ui.customer_field.text()) > 0
        reason_selected = self.ui.reasons_combo_box.currentText() != "Selecione"

        if self.reprint_frame_activated:
            if label_data_filled and reason_selected:
                WidgetHelper.enable_widget(self.ui.print_button)
            else:
                WidgetHelper.disable_widget(self.ui.print_button)
        else:
            if label_data_filled:
                WidgetHelper.enable_widget(self.ui.print_button)
            else:
                WidgetHelper.disable_widget(self.ui.print_button)

    def manage_clear_button(self) -> None:
        valid_info = len(self.ui.customer_field.text()) > 0

        if valid_info:
            WidgetHelper.enable_widget(self.ui.clear_button)
        else:
            WidgetHelper.disable_widget(self.ui.clear_button)

    def handle_users_management_button(self) -> None:
        self.users_management_window = UsersManagementView()
        self.users_management_window.setWindowModality(QtCore.Qt.ApplicationModal)  # Definindo como modal
        self.users_management_window.show()

    def handle_report_button(self) -> None:
        self.printed_labels_window = PrintedLabelsView()
        self.printed_labels_window.setWindowModality(QtCore.Qt.ApplicationModal)  # Definindo como modal
        self.printed_labels_window.show()

    def handle_print_button(self) -> None:

        order_number = self.ui.order_entry.text()

        label = {
            "customer": self.order_data["nome"],
            "store": self.ui.service_store_field.text(),
            "date": self.ui.label_date_field.text(),
            "user_id": self.ui.checker_field.text(),
            "volumes": int(self.ui.label_quantity_display.text()),
            "order_id": order_number,
            "is_reprint": False,
            "reprint_reason": None
        }

        if self.reprint_frame_activated:
            label["reprint_reason"] = self.ui.reasons_combo_box.currentText()
            label["is_reprint"] = True

        Printer.print_label(label)

        RepositoryManager.printer_logs_repository().create_printer_log(label)

        self.new_search()

    def manage_print_permissions(self) -> None:
        order_number = self.ui.order_entry.text()
        printed = RepositoryManager.printer_logs_repository().verify_reprint(order_number)

        self.disable_search_field()

        if printed:
            if "REPRINT LABELS" in self.user["permissions"]:
                self.activate_reprint_frame()
                self.load_label_data()
            else:
                DialogWindowManager.dialog().already_printed()
                self.new_search()
        else:
            self.load_label_data()

    def handle_change_password_button(self) -> None:
        self.change_password_window = ChangePasswordView()
        self.change_password_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.change_password_window.show()


if __name__ == "__main__":
    session = SessionHelper()
    session.set("user", {'user_id': 999, 'name': 'admin', 'permissions': ['MANAGE USERS', 'REPORT', 'REPRINT LABELS']})
    app = QApplication()
    window = LabelsPrinterView()
    window.show()
    app.exec()
