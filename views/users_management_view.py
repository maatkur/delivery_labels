from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from functools import partial

from database.repositories.repository_manager import RepositoryManager
from helpers import WidgetHelper
from ui import UsersManagementWindow
from components.dialog_window.dialog_window_manager import DialogWindowManager


class UsersManagementView(QMainWindow):

    def __init__(self) -> None:
        super(UsersManagementView, self).__init__(parent=None)
        self.ui = UsersManagementWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.users_permissions = None
        self.filtered_user_permission = None
        self.retrieve_and_load()
        self.connect_widget_actions()
        WidgetHelper.install_event_filters(
            self,
            [
                self.ui.user_code_entry,
                self.ui.name_input,
                self.ui.id_input,
                self.ui.password_input
             ]
        )
        self.retrieve_permissions()
        self.ui.add_user_button.clicked.connect(self.handle_add_user_button)

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
        if widget == self.ui.user_code_entry:
            self.filter_and_load()
        if widget == self.ui.id_input:
            self.ui.name_input.setFocus()
        if widget == self.ui.name_input:
            self.ui.password_input.setFocus()
        if widget == self.ui.password_input:
            if len(self.ui.id_input.text()) > 0 and len(self.ui.name_input.text()) > 0 and len(self.ui.password_input.text()) > 0:
                self.handle_add_user_button()

    def connect_widget_actions(self) -> None:
        self.ui.user_code_entry.textChanged.connect(self.manage_search_button)
        self.ui.clear_button.clicked.connect(self.handle_clear_button)
        self.ui.clear_button.clicked.connect(self.retrieve_and_load)
        self.ui.search_button.clicked.connect(self.filter_and_load)
        self.ui.add_user_button.clicked.connect(None)  # TODO Alterar para a função de adicionar usuário

    def retrieve_permissions(self) -> None:
        self.users_permissions = RepositoryManager.users_permissions_repository().get_all_users_with_permissions()

    def retrieve_and_load(self) -> None:
        self.retrieve_permissions()

        if len(self.users_permissions) > 0:
            self.load_table(self.users_permissions)

    from functools import partial

    def load_table(self, users_permissions: list) -> None:
        # Limpar entrada e tabela
        WidgetHelper.clear_widget(self.ui.user_code_entry)
        WidgetHelper.clear_table(self.ui.tableWidget)

        # Mapear permissões para colunas
        permission_columns = {
            "REPRINT LABELS": 2,  # Coluna para Reimpressão
            "REPORT": 3  # Coluna para Relatórios
        }

        # Definir número de linhas e colunas
        self.ui.tableWidget.setRowCount(len(users_permissions) - 1)  # Ignorar usuário de ID 999
        self.ui.tableWidget.setColumnCount(4)  # Código, Nome, Reimpressão, Relatórios

        for row, user_data in enumerate(users_permissions):
            # Configurar Código e Nome
            if user_data['user_id'] == 999:
                continue

            for col, value in enumerate([str(user_data['user_id']), user_data['user_name']]):
                item = QTableWidgetItem(value)
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # Centralizar o texto
                self.ui.tableWidget.setItem(row, col, item)

            # Adicionar permissões às colunas corretas
            for permission, col in permission_columns.items():
                # Verificar se a permissão está na lista de permissões do usuário
                has_permission = permission in user_data['permissions']

                # Criar checkbox para indicar o estado da permissão
                checkbox = QCheckBox()
                checkbox.setChecked(has_permission)

                # Conectar o evento de mudança de estado usando partial
                checkbox.stateChanged.connect(
                    partial(self.handle_checkbox_state_changed, row, col)
                )

                # Criar layout e adicionar checkbox com alinhamento central
                layout = QHBoxLayout()
                layout.addWidget(checkbox)
                layout.setAlignment(QtCore.Qt.AlignCenter)  # Centralizar o checkbox

                cell_widget = QWidget()
                cell_widget.setLayout(layout)

                # Adicionar o widget da célula à tabela
                self.ui.tableWidget.setCellWidget(row, col, cell_widget)

        self.adjust_table_header()

    def filter_user(self) -> None:
        # Obter o código do usuário da entrada
        user_code = self.ui.user_code_entry.text().strip()

        # Atualizar as permissões do banco de dados
        self.retrieve_permissions()

        # Filtrar as permissões com base no código do usuário
        self.filtered_user_permission = [
            user for user in self.users_permissions if str(user['user_id']) == user_code
        ]

    def filter_and_load(self) -> None:
        self.filter_user()
        self.load_table(self.filtered_user_permission)

    def handle_checkbox_state_changed(self, row, col, state) -> None:

        # Tradução do índice da coluna para o nome da permissão
        permission_map = {
            2: "REPRINT LABELS",  # Coluna Reimpressão
            3: "REPORT"  # Coluna Relatórios
        }

        # Obter o código do usuário e a permissão correspondente
        user_id = int(self.ui.tableWidget.item(row, 0).text())
        permission = permission_map.get(col)

        if not permission:
            return  # Nenhuma permissão correspondente à coluna

        # Determinar se a permissão deve ser adicionada ou removida
        add_permission = state == Qt.CheckState.Checked.Checked.value  # Qt.Checked indica que o checkbox foi marcado

        # Obter permissões atuais do usuário
        repo = RepositoryManager.users_permissions_repository()
        current_permissions = repo.get_user_permissions(user_id)

        # Atualizar lista de permissões
        if add_permission and permission not in current_permissions:
            current_permissions.append(permission)  # Adicionar permissão
        elif not add_permission and permission in current_permissions:
            current_permissions.remove(permission)  # Remover permissão

        # Atualizar permissões no banco de dados
        permission_ids = [
            repo.get_permission_id_by_name(perm) for perm in current_permissions
        ]
        success = repo.update_user_permissions(user_id, permission_ids)


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
        WidgetHelper.clear_widget(
            [
                self.ui.id_input,
                self.ui.name_input,
                self.ui.password_input
            ]
        )

    def handle_add_user_button(self):
        height = self.ui.widget.height()

        user_data_fields = [self.ui.id_input, self.ui.name_input, self.ui.password_input]
        has_user_data = all([len(field.text()) > 0 for field in user_data_fields])

        if height == 0:
            self.manage_widget_height()

        elif height > 0 and has_user_data:
            self.add_user()
            WidgetHelper.clear_widget(user_data_fields)
            self.manage_widget_height()

        elif height > 0 and not has_user_data:
            WidgetHelper.clear_widget(user_data_fields)
            self.manage_widget_height()

    def manage_widget_height(self) -> None:
        height = self.ui.widget.height()

        if height == 0:
            self.ui.widget.setMaximumHeight(16777215)
        else:
            self.ui.widget.setMaximumHeight(0)

    def add_user(self):
        user = {
            "id": self.ui.id_input.text(),
            "name": self.ui.name_input.text(),
            "password": self.ui.password_input.text()
        }

        user_has_created = RepositoryManager.users_repository().create_user_if_not_exists(user)

        if not user_has_created:
            DialogWindowManager.dialog().error("Usuário já cadastrado")
        else:
            DialogWindowManager.dialog().success("Usuário cadastrado com sucesso")
            self.retrieve_and_load()

    def adjust_table_header(self) -> None:
        self.ui.tableWidget.horizontalHeader().resizeSection(0, 100)
        self.ui.tableWidget.horizontalHeader().resizeSection(1, 120)
        self.ui.tableWidget.horizontalHeader().resizeSection(2, 98)
        self.ui.tableWidget.horizontalHeader().resizeSection(3, 79)


if __name__ == "__main__":
    app = QApplication()
    window = UsersManagementView()
    window.show()
    app.exec()
