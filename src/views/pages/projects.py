from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Projects_ui, Project_ui
from config import Pages
from main import MainWindow


class Project(QWidget, Project_ui.Ui_Element):
    def __init__(self, name: str):
        super().__init__()
        self.setupUi(self)
        self.lblProjectName.setText(name)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumHeight(42)


class Projects(QWidget, Projects_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def setPage(cls: MainWindow) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.projects["title"])
    cls.lblDescription.setText(Pages.projects["description"])
    widget = Projects(cls.frContent)
    return widget
