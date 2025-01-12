from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Projects_ui, Project_ui
from controllers import new_project
from config import Pages


class Project(QWidget, Project_ui.Ui_Element):
    def __init__(self, name: str):
        super().__init__()
        self.setupUi(self)
        self.lblProjectName.setText(name)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumHeight(42)


class Projects(QWidget, Projects_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.btnNew.clicked.connect(lambda: self.onBtnNewClicked(cls))

    def onBtnNewClicked(self, cls) -> None:
        widget = new_project.setPage(cls)
        cls.switchPage(widget)
        return


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.projects["title"])
    cls.lblDescription.setText(Pages.projects["description"])
    widget = Projects(cls)
    return widget
