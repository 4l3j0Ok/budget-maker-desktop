from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QLabel,
    QVBoxLayout,
    QFileDialog,
)
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWebEngineWidgets import QWebEngineView
from views.ui import (
    NewProject_ui,
    ProjectProduct_ui,
    NewProjectTemplate_ui,
    Success_ui,
    colors,
)
from config import Pages, Path
from utils import modify_button, get_template_list, render_template, create_pdf
from models.products import Product
from models.projects import Project


class ProjectProduct(QWidget, ProjectProduct_ui.Ui_Element):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupButtons()
        self.setupLineEdit()

    def setupButtons(self):
        modify_button(
            self.btnDelete,
            fg_color="white",
            bg_color=colors.Light.delete,
            bg_pressed_color=colors.Light.delete_alt,
        )
        modify_button(
            self.btnHide,
            fg_color="white",
        )
        modify_button(self.btnLock, fg_color="white")
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
                        fg_color="white",
                        icon=":/icons/views/assets/ic--outline-lock-open.svg"
                        if self.locked
                        else ":/icons/views/assets/ic--outline-lock.svg",
                    )
                elif element.objectName() == "btnDelete":
                    modify_button(
                        element,
                        bg_color=colors.Light.delete_alt
                        if self.locked
                        else colors.Light.delete,
                    )
                else:
                    modify_button(
                        element,
                        bg_color=colors.Light.accent_alt
                        if self.locked
                        else colors.Light.accent,
                    )
            elif isinstance(element, QLineEdit):
                element.setStyleSheet(
                    "background-color: #f0f0f0"
                    if self.locked
                    else "background-color: #ffffff"
                )

    def toggleVisibility(self):
        modify_button(
            self.sender(),
            fg_color="white",
            icon=":/icons/views/assets/eva--eye-off-2-outline.svg"
            if self.costVisible
            else ":/icons/views/assets/eva--eye-outline.svg",
        )
        self.costVisible = not self.costVisible

    def deleteLater(self):
        super().deleteLater()


class NewProject(QWidget, NewProject_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.setupButtons(cls)
        self.leTotal.setValidator(QRegularExpressionValidator(r"^[0-9]*$", self))

    def setupButtons(self, cls):
        self.btnAdd.clicked.connect(self.addProduct)
        self.btnClear.clicked.connect(lambda: self.reloadWidget(cls))
        self.btnNext.setEnabled(False)
        modify_button(self.btnNext, bg_color=colors.Light.deselected)
        self.btnNext.clicked.connect(
            lambda: cls.switchPage(
                NewProjectTemplate(
                    cls,
                    self.leProjectName.text(),
                    self.getProducts(),
                    self.leTotal.text(),
                    self,
                ),
                hide=True,
            )
        )

    def addProduct(self):
        widget = ProjectProduct()
        self.toggleNextButton(False)
        self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
        widget.leCost.textChanged.connect(lambda: self.checkLineEdits(True))
        widget.leProduct.textChanged.connect(lambda: self.checkLineEdits(False))
        widget.leQuantity.textChanged.connect(lambda: self.checkLineEdits(False))
        widget.btnDelete.clicked.connect(lambda: self.deleteProduct(widget))

    def deleteProduct(self, widget):
        widget.deleteLater()
        # Eliminamos el widget del layout porque deleteLater lo hace al siguiente ciclo de eventos.
        self.verticalLayout.removeWidget(widget)
        self.checkLineEdits(True)

    def checkLineEdits(self, update_total: bool) -> None:
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
        total = total if not str(total).endswith(".0") else int(total)
        self.leTotal.setText(str(total))

    def getProducts(self):
        products = []
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if widget and isinstance(widget, ProjectProduct):
                products.append(
                    Product(
                        name=widget.leProduct.text(),
                        quantity=int(widget.leQuantity.text()),
                        cost=float(widget.leCost.text()),
                        cost_visible=widget.costVisible,
                    )
                )
        return products

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
            bg_color=colors.Light.accent if enabled else colors.Light.deselected,
            bg_pressed_color=colors.Light.accent_alt
            if enabled
            else colors.Light.deselected_alt,
        )


# Templates de PDF que se pueden seleccionar para el proyecto.
class Template(QWidget):
    def __init__(self, html, name, file_name):
        super(Template, self).__init__()
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
            bg_color=colors.Light.deselected,
            bg_pressed_color=colors.Light.deselected_alt,
        )
        self.verticalLayout.addWidget(self.webView)
        self.verticalLayout.addWidget(self.lblProjectName)
        self.verticalLayout.addWidget(self.btnSelect)
        self.setLayout(self.verticalLayout)


# Ventana para seleccionar el template de PDF
class NewProjectTemplate(QWidget, NewProjectTemplate_ui.Ui_Form):
    def __init__(self, cls, project_name, products, total, parent_widget):
        super().__init__()
        self.setupUi(self)
        self.project_name = project_name
        self.products = products
        self.total = total
        modify_button(self.btnNext, bg_color=colors.Light.deselected)
        self.btnNext.setEnabled(False)
        self.btnBack.clicked.connect(lambda: cls.switchPage(parent_widget, hidden=True))
        self.btnNext.clicked.connect(lambda: self.onButtonNextClicked(cls))
        self.leProjectName.setText(self.project_name)
        self.gridLayout.setSpacing(10)
        self.templates = []
        for file_name in get_template_list():
            html = render_template(
                f"{Path.html_tpls}/{file_name}",
                project_name=self.project_name,
                items=self.products,
                total=self.total,
            )
            pretty_name = (
                file_name.replace(".html", "")
                .replace(".tpl", "")
                .replace("_", " ")
                .replace("-", " ")
                .title()
            )
            template = Template(html, pretty_name, file_name)
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
                bg_color=colors.Light.selected
                if is_selected
                else colors.Light.deselected,
                bg_pressed_color=colors.Light.selected_alt
                if is_selected
                else colors.Light.deselected_alt,
            )
            if is_selected:
                is_any_selected = True
        self.toggleNextButton(is_any_selected)

    def onButtonNextClicked(self, cls):
        html = next((template.html for template in self.templates if template.selected))
        # Guardar el proyecto en la base de datos
        self.project = Project(name=self.project_name, total=self.total)
        self.project.insert(cls.db)
        # Guardar los productos en la base de datos
        for product in self.products:
            product: Product
            product.project_id = self.project.project_id
            product.insert(cls.db)

        cls.switchPage(Success(cls, html=html))

    def toggleNextButton(self, enabled: bool) -> None:
        self.btnNext.setEnabled(enabled)
        modify_button(
            self.btnNext,
            bg_color=colors.Light.accent if enabled else colors.Light.deselected,
            bg_pressed_color=colors.Light.accent_alt
            if enabled
            else colors.Light.deselected_alt,
        )


class Success(QWidget, Success_ui.Ui_Form):
    def __init__(self, cls, html):
        super().__init__()
        self.setupUi(self)
        self.setupButtons()
        self.html = html

    def setupButtons(self):
        modify_button(
            self.btnHome,
            fg_color="white",
            bg_color=colors.Light.accent,
            bg_pressed_color=colors.Light.accent_alt,
        )
        modify_button(
            self.btnSavePDF,
            fg_color="white",
            bg_color=colors.Light.accent,
            bg_pressed_color=colors.Light.accent_alt,
        )
        self.btnSavePDF.clicked.connect(self.save_pdf)

    def save_pdf(self):
        # Mostramos el dialogo de guardado
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar PDF", "", "PDF Files (*.pdf)"
        )
        if file_path:
            create_pdf(self.html, file_path)
            modify_button(
                self.btnSavePDF,
                fg_color="white",
                bg_color=colors.Light.selected,
                bg_pressed_color=colors.Light.selected_alt,
            )


def setPage(cls) -> None:
    cls.lblTitle.setText(Pages.new_project["title"])
    cls.lblDescription.setText(Pages.new_project["description"])
    widget = NewProject(cls)
    return widget
