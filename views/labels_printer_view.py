from typing import Optional

from PySide6 import QtCore
from PySide6.QtWidgets import *

from components.dialog_window.dialog_window_manager import DialogWindowManager
from database.repositories.repository_manager import RepositoryManager
from helpers import SessionHelper
from helpers import WidgetHelper
from helpers.date_helper import DateHelper
from helpers.query_helper import QueryHelper
from helpers.sanitize_str_helper import SanitizeStrHelper
from ui import LabelPrinterWindow
from views.labels_report_view import PrintedLabelsView
from views.password_chage_view import ChangePasswordView
from views.users_management_view import UsersManagementView


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
        self.ui.reasons_combo_box.currentTextChanged.connect(self.manage_complement_combo_box)
        self.ui.complement_id_combo_box.currentTextChanged.connect(self.manage_print_button)
        self.ui.label_quantity_display.textEdited.connect(self.validate_quantity_input)
        self.ui.label_quantity_display.textEdited.connect(self.change_quantity_label)
        self.ui.reasons_combo_box.currentTextChanged.connect(self.manage_interval_entry)
        self.ui.interval_entry.textChanged.connect(self.validate_interval_input)

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
        if "MANAGE USERS" in self.user.permissions:
            if widget == self.ui.users_menu_button:
                self.handle_users_management_button()
        if "REPORT" in self.user.permissions:
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
        self.ui.complement_id_combo_box.setCurrentText("Selecione")

    def change_quantity_display(self, value) -> None:
        volume = int(self.ui.label_quantity_display.text() or "1")  # Default 1 se vazio
        volume += value
        if 1 <= volume <= 100:
            self.ui.label_quantity_display.setText(f"{volume}")

    def validate_quantity_input(self, text: str) -> None:
        # Se vazio, aceita (vai preencher depois)
        if not text:
            return

        # Tenta converter pra int
        try:
            volume = int(text)
            # Corrige se fora do limite
            if volume < 1:
                self.ui.label_quantity_display.setText("1")
            elif volume > 100:
                self.ui.label_quantity_display.setText("1")
        except ValueError:
            # Se não for número, volta pro último valor válido ou 1
            self.ui.label_quantity_display.setText("1")

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
        if self.order_data:
            volumes = RepositoryManager.printer_logs_repository().verify_reprint_volumes(order_number)
            if volumes is not None:
                self.ui.label_quantity_display.setText(str(volumes))
            else:
                self.ui.label_quantity_display.setText("1")  # Padrão para ordens novas
            self.manage_print_permissions()
        else:
            DialogWindowManager.dialog().search_error()
            self.new_search()

    def load_label_data(self) -> None:

        self.ui.customer_field.setText(self.order_data["nome"])
        self.ui.service_store_field.setText(
            SanitizeStrHelper.sanitize_str(self.order_data["loja"])
        )
        self.ui.label_date_field.setText(DateHelper.get_current_date())
        self.ui.checker_field.setText(f'{self.user.id}')

    def show_logged_user(self) -> None:

        self.ui.logged_user_label.setText(f"{self.user.id}-{self.user.name}")

    def disable_search_field(self) -> None:
        self.ui.order_entry.setDisabled(True)

    def enable_search_field(self) -> None:
        self.ui.order_entry.setDisabled(False)

    def manage_search_button(self) -> None:
        order_entry_filled = len(self.ui.order_entry.text()) > 0

        self.ui.search_button.setEnabled(order_entry_filled)

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
        if "MANAGE USERS" in self.user.permissions:
            WidgetHelper.enable_widget(self.ui.users_menu_button)
        else:
            WidgetHelper.disable_widget(self.ui.users_menu_button)

    def manage_report_button(self) -> None:
        can_access_reports = "REPORT" in self.user.permissions

        self.ui.reports_button.setEnabled(can_access_reports)

    def manage_print_button(self) -> None:
        label_data_filled = len(self.ui.customer_field.text()) > 0
        reason_selected = self.ui.reasons_combo_box.currentText() != "Selecione"

        if self.reprint_frame_activated:
            # Só prossegue se label_data_filled e reason_selected forem verdadeiros
            if label_data_filled and reason_selected:
                # Caso especial: "Pedido complementar/parcial"
                if self.ui.reasons_combo_box.currentText() == "Pedido complementar/parcial":
                    # Só ativa se complement_id for diferente de "Selecione"
                    if self.ui.complement_id_combo_box.currentText() != "Selecione":
                        WidgetHelper.enable_widget(self.ui.print_button)
                    else:
                        WidgetHelper.disable_widget(self.ui.print_button)
                # Outros motivos: ativa direto
                else:
                    WidgetHelper.enable_widget(self.ui.print_button)
            else:
                WidgetHelper.disable_widget(self.ui.print_button)
        else:
            # Fora do reprint_frame, só checa label_data_filled
            if label_data_filled:
                WidgetHelper.enable_widget(self.ui.print_button)
            else:
                WidgetHelper.disable_widget(self.ui.print_button)

    def manage_complement_combo_box(self) -> None:
        can_enable_complement_combo_box = self.ui.reasons_combo_box.currentText() == "Pedido complementar/parcial"

        self.ui.complement_id_combo_box.setEnabled(can_enable_complement_combo_box)

    def manage_clear_button(self) -> None:
        can_enable_clear_button = len(self.ui.customer_field.text()) > 0

        self.ui.clear_button.setEnabled(can_enable_clear_button)

    def manage_interval_entry(self) -> None:
        """
        Habilita o campo de entrada de intervalo se o motivo da reimpressão for válido.
        """

        self.ui.interval_entry.setText("")  # Limpa o campo de entrada de intervalo

        can_enable_interval_entry = self.ui.reasons_combo_box.currentText() in [
            "Falha na impressora",
            "Impressora sem etiqueta",
            "Impressora sem tinta (Ribbon)"  # Corrigido
        ]

        self.ui.interval_entry.setEnabled(can_enable_interval_entry)

    def validate_interval_input(self, text: str) -> None:
        """Valida o input do interval_entry no formato 'inicio;fim'."""
        if not text:
            self.ui.interval_entry.setStyleSheet(
                "background-color: rgb(57, 123, 201); border: 2px solid rgb(57, 123, 201); border-radius: 10px;")
            return

        try:
            start, end = map(int, text.split(";"))
            max_volumes = RepositoryManager.printer_logs_repository().verify_reprint_volumes(self.ui.order_entry.text())
            if max_volumes is None:
                raise ValueError("Ordem não encontrada ou sem impressão anterior")
            if start < 1 or end > max_volumes or start > end:
                raise ValueError("Intervalo inválido")
            self.ui.interval_entry.setStyleSheet(
                "background-color: rgb(57, 123, 201); border: 2px solid rgb(57, 123, 201); border-radius: 10px;")
        except ValueError:
            self.ui.interval_entry.setStyleSheet(
                "background-color: rgb(255, 100, 100); border: 2px solid rgb(255, 100, 100); border-radius: 10px;")


    def get_interval(self) -> Optional[tuple[int, int]]:
        """Retorna o intervalo do interval_entry ou None se vazio."""
        text = self.ui.interval_entry.text()
        if not text:
            return None
        try:
            start, end = map(int, text.split(";"))
            max_volumes = RepositoryManager.printer_logs_repository().verify_reprint_volumes(self.ui.order_entry.text())
            if max_volumes is None:
                raise ValueError("Ordem não encontrada ou sem impressão anterior")
            if 1 <= start <= end <= max_volumes:
                return start, end
            else:
                raise ValueError("Intervalo fora dos limites")
        except ValueError:
            DialogWindowManager.dialog().error("Intervalo inválido! Use o formato 'inicio;fim' (ex.: 7;10).")
            return None

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
        interval = self.get_interval()  # Pega o intervalo do interval_entry

        # Define volumes com base no motivo e intervalo
        if self.reprint_frame_activated and interval and self.ui.reasons_combo_box.currentText() in [
            "Falha na impressora",
            "Impressora sem etiqueta",
            "Impressora sem tinta (Ribbon)"
        ]:
            # Usa verify_reprint_volumes pra reimpressões com intervalo
            volumes = RepositoryManager.printer_logs_repository().verify_reprint_volumes(order_number)
            if volumes is None:
                DialogWindowManager.dialog().error("Ordem não encontrada no histórico para reimpressão com intervalo!")
                return
        else:
            # Usa label_quantity_display pra ordens novas ou reimpressões sem intervalo
            volumes = int(self.ui.label_quantity_display.text() or "1")

        label = {
            "customer": self.order_data["nome"],
            "store": self.ui.service_store_field.text(),
            "date": self.ui.label_date_field.text(),
            "user_id": self.ui.checker_field.text(),
            "volumes": volumes,
            "order_id": order_number,
            "is_reprint": False,
            "reprint_reason": None,
            "interval": interval
        }

        if self.reprint_frame_activated:
            label["reprint_reason"] = self.ui.reasons_combo_box.currentText()
            label["is_reprint"] = True

        if label["reprint_reason"] == "Pedido complementar/parcial":
            label["order_id"] = label["order_id"] + rf"/{self.ui.complement_id_combo_box.currentText()}"
        
        log_data = label.copy()
        
        for i in range(label["volumes"]):
            label["current_label"] = i + 1
            print(label)
            print("--------------------------------")
        if interval and log_data["is_reprint"]:
                log_data[
                        "reprint_reason"] = f"{log_data['reprint_reason']} (intervalo: {interval[0]};{interval[1]})"
                RepositoryManager.printer_logs_repository().create_printer_log(log_data)

        #Printer.print_label(label)
        
        self.new_search()

    def manage_print_permissions(self) -> None:
        order_number = self.ui.order_entry.text()
        printed = RepositoryManager.printer_logs_repository().verify_reprint(order_number)

        self.disable_search_field()

        if printed:
            if "REPRINT LABELS" in self.user.permissions:
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
