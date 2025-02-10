from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QLabel,
    QVBoxLayout,
)
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWebEngineWidgets import QWebEngineView
from views.ui import (
    NewProject_ui,
    ProjectProduct_ui,
    NewProjectTemplate_ui,
    Success_ui,
)
from config import Pages, Path
from utils import modify_button, get_template_list, render_template, save_pdf
from models.products import ProductModel
from models.projects import ProjectModel
from controllers import projects


class ProjectProduct(QWidget, ProjectProduct_ui.Ui_Element):
    def __init__(
        self, db, selected_color, project_id: int, product_id: int | None = None
    ):
        super().__init__()
        self.setupUi(self)
        self.selected_color = selected_color
        self.setupButtons()
        self.setupLineEdit()
        self.db_object = (
            ProductModel(db, project_id=project_id)
            if not product_id
            else ProductModel.get(
                db,
                product_id=product_id,
            )
        )

    def setupButtons(self):
        modify_button(
            self.btnDelete,
            fg_color=self.selected_color.button_text_alt,
            bg_color=self.selected_color.delete,
            bg_pressed_color=self.selected_color.delete_alt,
        )
        modify_button(
            self.btnHide,
            fg_color=self.selected_color.button_text_alt,
        )
        modify_button(self.btnLock, fg_color=self.selected_color.button_text_alt)
        self.locked = False
        self.costVisible = True
        self.btnLock.clicked.connect(self.toggleLock)
        self.btnHide.clicked.connect(self.toggleVisibility)

    def setupLineEdit(self):
        self.leQuantity.setValidator(QRegularExpressionValidator(r"^[0-9]*$", self))
        self.leCost.setValidator(
            QRegularExpressionValidator(r"^[0-9]*[.,]?[0-9]*$", self)
        )

    def toggleLock(self):
        self.locked = not self.locked
        self.btnDelete.setEnabled(not self.locked)
        self.leQuantity.setEnabled(not self.locked)
        self.leProduct.setEnabled(not self.locked)
        self.leCost.setEnabled(not self.locked)
        for element in self.findChildren(QWidget):
            if isinstance(element, QPushButton):
                if element.objectName() == "btnLock":
                    modify_button(
                        element,
                        fg_color=self.selected_color.button_text_alt,
                        icon=":/icons/views/assets/ic--outline-lock-open.svg"
                        if self.locked
                        else ":/icons/views/assets/ic--outline-lock.svg",
                    )
                elif element.objectName() == "btnDelete":
                    modify_button(
                        element,
                        bg_color=self.selected_color.delete_alt
                        if self.locked
                        else self.selected_color.delete,
                    )
                else:
                    modify_button(
                        element,
                        bg_color=self.selected_color.accent_alt
                        if self.locked
                        else self.selected_color.accent,
                    )
            elif isinstance(element, QLineEdit):
                element.setStyleSheet(
                    f"background-color: {self.selected_color.le_disabled}"
                    if self.locked
                    else f"background-color: {self.selected_color.le_enabled}"
                )

    def toggleVisibility(self):
        modify_button(
            self.sender(),
            fg_color=self.selected_color.button_text_alt,
            icon=":/icons/views/assets/eva--eye-off-2-outline.svg"
            if self.costVisible
            else ":/icons/views/assets/eva--eye-outline.svg",
        )
        self.costVisible = not self.costVisible
        self.db_object.cost_visible = self.costVisible
        self.db_object.update()

    def deleteLater(self):
        super().deleteLater()


class NewProject(QWidget, NewProject_ui.Ui_Form):
    def __init__(self, cls, db_object: ProjectModel | None = None):
        super().__init__()
        self.setupUi(self)
        self.selected_color = cls.selected_color
        self.setupButtons(cls)
        self.db_object = ProjectModel(cls.db) if not db_object else db_object
        self.leTotal.setValidator(QRegularExpressionValidator(r"^[0-9]*$", self))
        pretty_total = (
            str(self.db_object.total)
            if not str(self.db_object.total).endswith(".0")
            else str(int(self.db_object.total))
        )
        self.leTotal.setText(pretty_total)
        self.leTotal.textChanged.connect(self.updateTotalDB)
        self.leProjectName.setText(self.db_object.name)
        self.leProjectName.textChanged.connect(self.updateNameDB)
        for product in ProductModel.get(cls.db, project_id=self.db_object.project_id):
            pretty_cost = (
                str(product.cost)
                if not str(product.cost).endswith(".0")
                else str(int(product.cost))
            )
            self.addProduct(
                cls.db,
                cost=pretty_cost,
                name=product.name,
                quantity=str(product.quantity),
                product_id=product.product_id,
            )
        self.checkLineEdits(self, update_total=False, db_update=False)

    def setupButtons(self, cls):
        self.btnAdd.clicked.connect(lambda: self.addProduct(cls.db))
        self.btnClear.clicked.connect(lambda: self.reloadWidget(cls))
        self.btnNext.setEnabled(False)
        modify_button(self.btnNext, bg_color=self.selected_color.deselected)
        self.btnNext.clicked.connect(
            lambda: cls.switchPage(
                NewProjectTemplate(cls, parent_widget=self, db_object=self.db_object),
                hide=True,
            )
        )

    def addProduct(
        self,
        db,
        cost: str = "",
        name: str = "",
        quantity: str = "",
        product_id: int = None,
    ):
        widget = ProjectProduct(
            db,
            self.selected_color,
            project_id=self.db_object.project_id,
            product_id=product_id,
        )
        self.toggleNextButton(False)
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
        widget.leProduct.setText(name)
        widget.leQuantity.setText(quantity)
        widget.leCost.setText(cost)
        widget.leCost.textChanged.connect(lambda: self.checkLineEdits(widget, True))
        widget.leProduct.textChanged.connect(lambda: self.checkLineEdits(widget))
        widget.leQuantity.textChanged.connect(lambda: self.checkLineEdits(widget))
        widget.btnDelete.clicked.connect(lambda: self.deleteProduct(widget))

    def deleteProduct(self, widget):
        widget.db_object.delete()
        widget.deleteLater()
        self.verticalLayout.removeWidget(widget)
        self.checkLineEdits(True, db_update=False)

    def checkLineEdits(
        self, widget: ProjectProduct, update_total: bool = False, db_update: bool = True
    ) -> None:
        if db_update:
            widget.db_object.name = widget.leProduct.text()
            widget.db_object.quantity = (
                widget.leQuantity.text() if widget.leQuantity.text() else 0
            )
            widget.db_object.cost = widget.leCost.text() if widget.leCost.text() else 0
            widget.db_object.update()
        line_edits_values = []
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if widget and isinstance(widget, ProjectProduct):
                line_edits_values.append(widget.leProduct.text())
                line_edits_values.append(widget.leQuantity.text())
                line_edits_values.append(widget.leCost.text())
        self.toggleNextButton(all(line_edits_values))
        if update_total:
            self.updateTotal()

    def updateTotal(self) -> None:
        total = 0
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if widget and isinstance(widget, ProjectProduct):
                widget.leCost.setText(widget.leCost.text().replace(",", "."))
                cost = float(widget.leCost.text()) if widget.leCost.text() else 0
                total += cost
        pretty_total = str(total) if not str(total).endswith(".0") else str(int(total))
        self.leTotal.setText(pretty_total)

    def updateTotalDB(self, total) -> None:
        self.db_object.total = total
        self.db_object.update()

    def updateNameDB(self, name) -> None:
        self.db_object.name = name
        self.db_object.update()

    def reloadWidget(self, cls) -> None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Limpiar formulario")
        msg.setText("¿Estás seguro de que deseas limpiar el formulario?")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        response = msg.exec()
        if response == QMessageBox.StandardButton.No:
            return
        widget = setPage(cls)
        cls.switchPage(widget)

    def toggleNextButton(self, enabled: bool) -> None:
        self.btnNext.setEnabled(enabled)
        modify_button(
            self.btnNext,
            bg_color=self.selected_color.accent
            if enabled
            else self.selected_color.deselected,
            bg_pressed_color=self.selected_color.accent_alt
            if enabled
            else self.selected_color.deselected_alt,
        )


class Template(QWidget):
    def __init__(self, html, name, file_name, selected_color):
        super(Template, self).__init__()
        self.selected_color = selected_color
        self.file_name = file_name
        self.selected = False
        self.verticalLayout = QVBoxLayout(self)
        self.webView = QWebEngineView()
        self.html = html
        self.webView.setHtml(self.html)
        self.lblProjectName = QLabel()
        self.lblProjectName.setText(name)
        self.btnSelect = QPushButton()
        self.btnSelect.setText("Seleccionar")
        modify_button(
            self.btnSelect,
            bg_color=self.selected_color.deselected,
            bg_pressed_color=self.selected_color.deselected_alt,
        )
        self.verticalLayout.addWidget(self.webView)
        self.verticalLayout.addWidget(self.lblProjectName)
        self.verticalLayout.addWidget(self.btnSelect)
        self.setLayout(self.verticalLayout)


# Ventana para seleccionar el template de PDF
class NewProjectTemplate(QWidget, NewProjectTemplate_ui.Ui_Form):
    def __init__(self, cls, parent_widget, db_object: ProjectModel):
        super().__init__()
        self.setupUi(self)
        self.selected_color = cls.selected_color
        self.db_object = db_object
        modify_button(self.btnNext, bg_color=self.selected_color.deselected)
        self.btnNext.setEnabled(False)
        self.btnBack.clicked.connect(lambda: cls.switchPage(parent_widget, hidden=True))
        self.btnNext.clicked.connect(lambda: self.onButtonNextClicked(cls))
        self.leProjectName.setText(self.db_object.name)
        self.gridLayout.setSpacing(10)
        self.templates = []
        pretty_total = (
            self.db_object.total
            if not str(self.db_object.total).endswith(".0")
            else int(self.db_object.total)
        )
        products = []
        for product in ProductModel.get(cls.db, project_id=self.db_object.project_id):
            pretty_cost = (
                product.cost
                if not str(product.cost).endswith(".0")
                else int(product.cost)
            )
            product.cost = pretty_cost
            products.append(product)
        for file_name in get_template_list():
            html = render_template(
                f"{Path.html_tpls}/{file_name}",
                project_name=self.db_object.name,
                items=products,
                total=pretty_total,
            )
            pretty_name = (
                file_name.replace(".html", "")
                .replace(".tpl", "")
                .replace("_", " ")
                .replace("-", " ")
                .title()
            )
            template = Template(html, pretty_name, file_name, self.selected_color)
            template.btnSelect.clicked.connect(self.onButtonSelectClicked)
            self.templates.append(template)
            self.gridLayout.addWidget(template, 0, self.gridLayout.columnCount())

    def onButtonSelectClicked(self):
        sender = self.sender()
        is_any_selected = False
        for template in self.templates:
            is_current = template.btnSelect == sender
            is_selected = is_current and not template.selected
            template.selected = is_selected
            template.btnSelect.setText("Seleccionado" if is_selected else "Seleccionar")
            modify_button(
                template.btnSelect,
                bg_color=self.selected_color.selected
                if is_selected
                else self.selected_color.deselected,
                bg_pressed_color=self.selected_color.selected_alt
                if is_selected
                else self.selected_color.deselected_alt,
            )
            if is_selected:
                is_any_selected = True
        self.toggleNextButton(is_any_selected)

    def onButtonNextClicked(self, cls):
        """Actualiza el template seleccionado en la base de datos y cambia a la página de éxito."""
        html = next((template.html for template in self.templates if template.selected))
        self.db_object.template = next(
            (template.file_name for template in self.templates if template.selected)
        )
        self.db_object.update()
        cls.switchPage(Success(cls, html=html))

    def toggleNextButton(self, enabled: bool) -> None:
        self.btnNext.setEnabled(enabled)
        modify_button(
            self.btnNext,
            bg_color=self.selected_color.accent
            if enabled
            else self.selected_color.deselected,
            bg_pressed_color=self.selected_color.accent_alt
            if enabled
            else self.selected_color.deselected_alt,
        )


class Success(QWidget, Success_ui.Ui_Form):
    def __init__(self, cls, html):
        super().__init__()
        self.setupUi(self)
        self.selected_color = cls.selected_color
        self.setupButtons(cls)
        self.html = html

    def setupButtons(self, cls):
        modify_button(
            self.btnHome,
            fg_color=self.selected_color.button_text_alt,
            bg_color=self.selected_color.accent,
            bg_pressed_color=self.selected_color.accent_alt,
        )
        modify_button(
            self.btnSavePDF,
            fg_color=self.selected_color.button_text_alt,
            bg_color=self.selected_color.accent,
            bg_pressed_color=self.selected_color.accent_alt,
        )
        self.btnSavePDF.clicked.connect(
            lambda: save_pdf(cls, self.btnSavePDF, self.html)
        )
        self.btnHome.clicked.connect(lambda: cls.switchPage(projects.setPage(cls)))


def setPage(cls, project_db=None) -> None:
    cls.lblTitle.setText(Pages.new_project["title"])
    cls.lblDescription.setText(Pages.new_project["description"])
    widget = NewProject(cls, db_object=project_db)
    return widget
