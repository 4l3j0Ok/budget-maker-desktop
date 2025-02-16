from PySide6.QtWidgets import QWidget
from views.ui import Home_ui
from config import Pages


class Home(QWidget, Home_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.home["title"])
    cls.lblDescription.setText(Pages.home["description"])
    widget = Home(cls)
    return widget
