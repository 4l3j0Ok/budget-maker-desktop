from PySide6.QtWidgets import QWidget, QSizePolicy, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from config import Pages
from utils import modify_button
from views.ui import Product_ui, Products_ui
from models.products import ProductModel
from logger import logger


class Product(QWidget, Product_ui.Ui_Element):
    def __init__(self, db, selected_color, new=False, pid=None, name="", cost=""):
        super().__init__()
        self.db = db
        self.selected_color = selected_color
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumHeight(42)
        self.setupButtons()
        self.setupProjectBox()
        self.leName.setText(name)
        self.lePrice.setText(str(cost))
        self.lePrice.setValidator(QRegularExpressionValidator(r"^[0-9]*$", self))
        self.pid = pid
        if not new:
            self.toggleLock()

    def setupButtons(self):
        modify_button(
            self.btnDelete,
            fg_color=self.selected_color.button_text_alt,
            bg_color=self.selected_color.delete,
            bg_pressed_color=self.selected_color.delete_alt,
        )
        modify_button(
            self.btnEdit,
            icon=":/icons/views/assets/ic--baseline-done.svg",
            fg_color=self.selected_color.button_text_alt,
            bg_color="green",
        )
        self.btnEdit.clicked.connect(self.toggleEdit)
        self.btnDelete.clicked.connect(self.delete)

    def setupProjectBox(self):
        style_sheet = f"""
            QFrame {{
                background-color: {self.selected_color.card_background};
                border-radius: 5px;
                border: 1px solid {self.selected_color.card_border};
            }}
            QLabel {{
                border: none;
            }}
        """
        self.frBox.setStyleSheet(style_sheet)

    def toggleEdit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Faltan datos")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        if self.leName.text() == "":
            msg.setText("Completa el campo Nombre")
            msg.exec()
            return
        if self.lePrice.text() == "":
            msg.setText("Completa el campo Precio")
            msg.exec()
            return
        self.save()
        self.toggleLock()

    def toggleLock(self):
        self.leName.setEnabled(not self.leName.isEnabled())
        self.lePrice.setEnabled(not self.lePrice.isEnabled())
        self.leName.setStyleSheet(
            "background-color: #f0f0f0"
            if not self.leName.isEnabled()
            else "background-color: #ffffff"
        )
        self.lePrice.setStyleSheet(
            "background-color: #f0f0f0"
            if not self.leName.isEnabled()
            else "background-color: #ffffff"
        )
        modify_button(
            self.btnEdit,
            icon=":/icons/views/assets/ic--baseline-done.svg"
            if self.leName.isEnabled()
            else ":/icons/views/assets/ic--outline-edit.svg",
            fg_color=self.selected_color.button_text_alt,
            bg_color="green" if self.leName.isEnabled() else self.selected_color.accent,
        )

    def save(self):
        try:
            if not self.pid:
                self.pid = ProductModel.insert(
                    self.db,
                    self.leName.text(),
                    self.lePrice.text(),
                )
                return
            ProductModel.update(
                self.db,
                self.leName.text(),
                self.lePrice.text(),
                self.pid,
            )
        except Exception as ex:
            logger.exception(ex)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error al guardar")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Error al guardar el producto")
            msg.exec()
            return

    def delete(self):
        if self.pid:
            try:
                ProductModel.delete(self.db, self.pid)
            except Exception as ex:
                logger.exception(ex)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setWindowTitle("Error al eliminar")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setText("Error al eliminar el producto")
                msg.exec()
                return
        super().deleteLater()


class Products(QWidget, Products_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.db = cls.db
        self.selected_color = cls.selected_color
        self.btnNew.clicked.connect(self.onBtnNewClicked)
        self.loadProducts()

    def loadProducts(self):
        products = ProductModel.get_all(self.db)
        for product in products:
            widget = Product(
                self.db, self.selected_color, name=product.name, cost=product.cost
            )
            self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)

    def onBtnNewClicked(self) -> None:
        widget = Product(self.db, self.selected_color, new=True)
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)


def setPage(cls) -> None:
    cls.lblTitle.setText(Pages.products["title"])
    cls.lblDescription.setText(Pages.products["description"])
    widget = Products(cls)
    return widget
