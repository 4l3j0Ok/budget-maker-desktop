from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Product_ui, Products_ui
from config import Pages
from utils import set_button_color


class Product(QWidget, Product_ui.Ui_Element):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumHeight(42)
        set_button_color("white", self.btnDelete)


class Products(QWidget, Products_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnNew.clicked.connect(self.onBtnNewClicked)

    def onBtnNewClicked(self) -> None:
        widget = Product()
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
        return


def setPage(cls) -> None:
    cls.lblTitle.setText(Pages.products["title"])
    cls.lblDescription.setText(Pages.products["description"])
    widget = Products(cls.frContent)
    return widget
