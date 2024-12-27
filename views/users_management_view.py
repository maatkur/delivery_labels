from PySide6 import QtCore
from PySide6.QtWidgets import *
from dotenv import load_dotenv

from ui import UsersManagementWindow

from database.repositories.repository_manager import RepositoryManager
from components.dialog_window.dialog_window_manager import DialogWindowManager

load_dotenv(r'C:\Users\mathe\PycharmProjects\delivery_labels\config\development.env')


class UsersManagementView(QMainWindow):

    def __init__(self) -> None:
        super(UsersManagementView, self).__init__(parent=None)
        self.ui = UsersManagementWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.users_permissions = None
        self.filtered_user_permission = None
        self.retrieve_and_load()
        self.connect_widget_actions()
        WidgetHelper.install_event_filters(self,
                                           [self.ui.user_code_entry]
                                           )

    def eventFilter(self, widget, event) -> bool:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
                self.handle_enter_key(widget)
                return True  # Indica que o evento foi tratado
        return super().eventFilter(widget, event)

    def handle_enter_key(self, widget) -> None:
        if widget == self.ui.user_code_entry:
            self.filter_and_load()

    def connect_widget_actions(self) -> None:
        self.ui.user_code_entry.textChanged.connect(self.manage_search_button)
        self.ui.clear_button.clicked.connect(self.handle_clear_button)
        self.ui.clear_button.clicked.connect(self.retrieve_and_load)
        self.ui.search_button.clicked.connect(self.filter_and_load)
        self.ui.update_users_button.clicked.connect(self.handle_users_update_button)

    def retrieve_permissions(self) -> None:
        self.users_permissions = RepositoryManager.users_permissions_repository().get_all_permissions()

    def retrieve_and_load(self) -> None:
        self.retrieve_permissions()

        if len(self.users_permissions) > 0:

            self.load_table(self.users_permissions)

    def load_table(self, users_permissions: list) -> None:
        WidgetHelper.clear_widget(self.ui.user_code_entry)
        WidgetHelper.clear_table(self.ui.tableWidget)

        # Definir o número de linhas e colunas
        self.ui.tableWidget.setRowCount(len(users_permissions))
        self.ui.tableWidget.setColumnCount(len(users_permissions[0]))

        # Preencher os users_permissions
        for row, row_data in enumerate(users_permissions):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))

                # Defina o item da célula da tabela
                self.ui.tableWidget.setItem(row, col, item)  # Define o item na tabela

                if col == 2 or col == 3:
                    checkbox = QCheckBox()

                    checkbox.setChecked(value)  # Define o estado da caixa de seleção com base no valor

                    checkbox.stateChanged.connect(
                        lambda state, row=row, col=col: self.handle_checkbox_state_changed(row, col, state))

                    # Crie um layout horizontal para alinhar a caixa de seleção
                    layout = QHBoxLayout()
                    layout.addWidget(checkbox)

                    # Adicione o layout (contendo a caixa de seleção) à célula da tabela
                    cell_widget = QWidget()
                    cell_widget.setLayout(layout)
                    self.ui.tableWidget.setCellWidget(row, col, cell_widget)
        self.adjust_table_header()

    def filter_user(self) -> None:
        user_code = self.ui.user_code_entry.text()

        self.retrieve_permissions()

        filtered = list(filter(lambda x: str(x[0]) == user_code, self.users_permissions))

        self.filtered_user_permission = filtered

    def filter_and_load(self) -> None:
        self.filter_user()
        self.load_table(self.filtered_user_permission)

    def handle_checkbox_state_changed(self, row, col, state) -> None:

        translate = {
            2: "reprint",
            3: "report_access"
        }

        options = {
            "permission": translate[col],
            "value": 1 if state == 2 else 0,
            "code": self.ui.tableWidget.item(row, 0).text()
        }

        RepositoryManager.users_permissions_repository().update_user_permission(options)

    def enable_search_button(self) -> None:
        self.ui.search_button.setDisabled(False)

    def disable_search_button(self) -> None:
        self.ui.search_button.setDisabled(True)

    def manage_search_button(self) -> None:
        search_entry_filled = len(self.ui.user_code_entry.text()) > 0

        if search_entry_filled:
            self.enable_search_button()
        else:
            self.disable_search_button()

    def handle_clear_button(self) -> None:
        WidgetHelper.clear_widget(self.ui.user_code_entry)
        WidgetHelper.clear_table(self.ui.tableWidget)

    def handle_users_update_button(self) -> None:
        result = DialogWindowManager.dialog().confirmation()
        if result == QMessageBox.Yes:
            UserUpdateHelper.update_users()
            self.retrieve_and_load()

    def adjust_table_header(self) -> None:

        self.ui.tableWidget.horizontalHeader().resizeSection(0, 10)
        self.ui.tableWidget.horizontalHeader().resizeSection(1, 170)
        self.ui.tableWidget.horizontalHeader().resizeSection(2, 98)
        self.ui.tableWidget.horizontalHeader().resizeSection(3, 79)


if __name__ == "__main__":
    app = QApplication()
    window = UsersManagementView()
    window.show()
    app.exec()
