from PySide6.QtWidgets import QWidget
from views.ui import About_ui
from config import Pages, Application


class About(QWidget, About_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lblTitle.setText(self.lblTitle.text().format(version=Application.version))


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.about["title"])
    cls.lblDescription.setText(Pages.about["description"])
    widget = About()
    return widget
