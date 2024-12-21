from PySide6.QtWidgets import QWidget
from views.ui import NewProject_ui, ProjectProduct_ui
from config import Pages
from utils import set_button_color


class ProjectProduct(QWidget, ProjectProduct_ui.Ui_Element):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        set_button_color("white", self.btnDelete)
        set_button_color("white", self.btnLock)


class NewProject(QWidget, NewProject_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.addProject)

    def addProject(self):
        widget = ProjectProduct()
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
        return


def setPage(cls) -> None:
    cls.lblTitle.setText(Pages.new_project["title"])
    cls.lblDescription.setText(Pages.new_project["description"])
    widget = NewProject(cls.frContent)
    return widget
