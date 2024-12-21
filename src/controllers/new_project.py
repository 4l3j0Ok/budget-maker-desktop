from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton
from views.ui import NewProject_ui, ProjectProduct_ui, colors
from config import Pages
from utils import modify_button


class ProjectProduct(QWidget, ProjectProduct_ui.Ui_Element):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        modify_button(self.btnDelete, fg_color="white")
        modify_button(self.btnLock, fg_color="white")


class NewProject(QWidget, NewProject_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.addProduct)

    def addProduct(self):
        widget = ProjectProduct()
        widget.locked = False
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
        widget.btnDelete.clicked.connect(lambda: self.deleteProduct(widget))
        widget.btnLock.clicked.connect(lambda: self.toggleLock(widget))
        return

    def toggleLock(self, widget: ProjectProduct):
        widget.locked = not widget.locked
        widget.btnDelete.setEnabled(not widget.locked)
        widget.leAmount.setEnabled(not widget.locked)
        widget.leProduct.setEnabled(not widget.locked)
        widget.leTotal.setEnabled(not widget.locked)
        for element in widget.findChildren(QWidget):
            if isinstance(element, QPushButton):
                if element.objectName() == "btnLock":
                    modify_button(
                        element,
                        fg_color="white",
                        icon=":/icons/views/assets/ic--outline-lock-open.svg"
                        if widget.locked
                        else ":/icons/views/assets/ic--outline-lock.svg",
                    )
                if element.objectName() == "btnDelete":
                    modify_button(
                        element,
                        bg_color=colors.Light.delete_alt
                        if widget.locked
                        else colors.Light.delete,
                    )
            elif isinstance(element, QLineEdit):
                element.setStyleSheet(
                    "background-color: #f0f0f0"
                    if widget.locked
                    else "background-color: #ffffff"
                )
        return

    def deleteProduct(self, widget):
        self.verticalLayout.removeWidget(widget)
        widget.deleteLater()
        return


def setPage(cls) -> None:
    cls.lblTitle.setText(Pages.new_project["title"])
    cls.lblDescription.setText(Pages.new_project["description"])
    widget = NewProject(cls.frContent)
    return widget
