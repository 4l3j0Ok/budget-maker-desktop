from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Product_ui, Products_ui
from config import Pages


class Product(QWidget, Product_ui.Ui_Element):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumHeight(42)


class Products(QWidget, Products_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnNew.clicked.connect(self.onBtnNewClicked)

    def onBtnNewClicked(self) -> None:
        widget = Product()
        self.scrollAreaWidgetContents.layout().insertWidget(0, widget)
        return


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.products["title"])
    cls.lblDescription.setText(Pages.products["description"])
    widget = Products(cls.frContent)
    return widget
