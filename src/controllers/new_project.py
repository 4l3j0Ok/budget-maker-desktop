from PySide6.QtWidgets import QWidget
from views.ui import NewProject_ui
from config import Pages
from main import MainWindow


class NewProject(QWidget, NewProject_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def setPage(cls: MainWindow) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.new_project["title"])
    cls.lblDescription.setText(Pages.new_project["description"])
    widget = NewProject(cls.frContent)
    return widget
