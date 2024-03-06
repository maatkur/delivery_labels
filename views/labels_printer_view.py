from PySide6 import QtCore
from PySide6.QtWidgets import *
from ui import LabelPrinterWindow

from helpers import WidgetHelper
from helpers import LoggedUserHelper
from helpers.date_helper import get_current_date


from components.dialog_window.dialog_window_manager import DialogWindowManager

from database.repositories.repository_manager import RepositoryManager


class LabelsPrinterView(QMainWindow):

    def __init__(self) -> None:
        super(LabelsPrinterView, self).__init__(parent=None)
        self.ui = LabelPrinterWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.user = LoggedUserHelper.logged_user().get()
        print(self.user)
        self.show_logged_user()
        self.order_data = None
        self.orders_update_window = None
        self.manage_admin_widgets()
        WidgetHelper.install_event_filters(self, [
            self.ui.menu_button,
            self.ui.order_entry,
            self.ui.search_button,
            self.ui.clear_button,
            self.ui.print_button,
            self.ui.users_menu_button,
            self.ui.reports_button,
            self.ui.layout_options_button,
            self.ui.increment_button,
            self.ui.decrement_button
        ]
                                           )

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
            self.clear_order_fields()
        if widget == self.ui.search_button:
            self.search_order()

    def manage_drawer(self) -> None:
        drawer_closed = self.ui.drawer.width() == 0

        if drawer_closed:
            self.ui.drawer.setMinimumWidth(49)
        else:
            self.ui.drawer.setMinimumWidth(0)

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

    def manage_admin_widgets(self) -> None:
        widgets = [
            self.ui.users_menu_button,
            self.ui.reports_button
        ]

        if self.user["permissions"]["admin"]:
            WidgetHelper.enable_widget(widgets)
        else:
            WidgetHelper.disable_widget(widgets)

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

    def clear_order_fields(self) -> None:

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

    def search_order(self) -> None:
        order_number = self.ui.order_entry.text()
        self.order_data = RepositoryManager.orders_repository().get_order(order_number)

        if self.order_data:
            self.load_label_data()
        else:
            DialogWindowManager.dialog().search_error()

    def load_label_data(self) -> None:

        self.ui.customer_field.setText(self.order_data["customer"])
        self.ui.service_store_field.setText(self.order_data["store"])
        self.ui.label_date_field.setText(get_current_date())
        self.ui.checker_field.setText(f'{self.user["code"]}')

    def show_logged_user(self) -> None:

        self.ui.logged_user_label.setText(f"{self.user['code']}-{self.user['name']}")


if __name__ == "__main__":
    app = QApplication()
    window = LabelsPrinterView()
    window.show()
    app.exec()

