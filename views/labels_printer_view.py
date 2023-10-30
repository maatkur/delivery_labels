from PySide6 import QtCore
from PySide6.QtWidgets import *
from ui import LabelPrinterWindow

from helpers import WidgetHelper


class LabelsPrinterView(QMainWindow):

    def __init__(self) -> None:
        super(LabelsPrinterView, self).__init__(parent=None)
        self.ui = LabelPrinterWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        WidgetHelper.install_event_filters(self, [
            self.ui.menu_button,
            self.ui.order_entry,
            self.ui.search_button,
            self.ui.clear_button,
            self.ui.print_button,
            self.ui.users_menu_button,
            self.ui.reports_button,
            self.ui.update_orders_button
        ]
                                           )

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
                pass
                return True  # Indica que o evento foi tratado
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            self.handle_mouse_click(widget)
        return super().eventFilter(widget, event)

    def handle_mouse_click(self, widget):
        if widget == self.ui.menu_button:
            self.manage_drawer()

    def manage_drawer(self) -> None:
        drawer_closed = self.ui.drawer.width() == 0

        if drawer_closed:
            self.ui.drawer.setMinimumWidth(49)
        else:
            self.ui.drawer.setMinimumWidth(0)


if __name__ == "__main__":
    app = QApplication()
    window = LabelsPrinterView()
    window.show()
    app.exec()
