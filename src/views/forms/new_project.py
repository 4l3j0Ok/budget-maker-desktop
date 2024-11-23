from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import NewProject_ui as NewProject


class NewProject(QWidget, NewProject.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
