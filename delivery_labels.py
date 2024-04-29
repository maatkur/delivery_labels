from PySide6.QtWidgets import QApplication

from views.labels_login_view import LabelsLoginView

from helpers.path_helper import PathHelper

PathHelper.set_main_execution(True)

app = QApplication()
window = LabelsLoginView()
window.show()
app.exec()

