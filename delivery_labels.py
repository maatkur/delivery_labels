from PySide6.QtWidgets import QApplication

from views.labels_login_view import LabelsLoginView

app = QApplication()
window = LabelsLoginView()
window.show()
app.exec()

