from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Projects_ui, Project_ui, Preview_ui
from controllers import new_project
from models.projects import ProjectModel
from models.products import ProductModel
from config import Pages, Path
from utils import modify_button, render_template, save_pdf


class Project(QWidget, Project_ui.Ui_Element):
    def __init__(self, db, selected_color, project_id: int):
        super().__init__()
        self.setupUi(self)
        self.selected_color = selected_color
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setupProjectBox()
        self.setupButtons()
        self.db_object = ProjectModel.get(db, project_id)
        self.lblProjectName.setText(self.db_object.name)

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

    def setupButtons(self):
        modify_button(
            self.btnEdit,
            fg_color="white",
            bg_color=self.selected_color.accent,
            bg_pressed_color=self.selected_color.accent_alt,
        )
        modify_button(
            self.btnPreview,
            fg_color="white",
            bg_color=self.selected_color.accent,
            bg_pressed_color=self.selected_color.accent_alt,
        )
        modify_button(
            self.btnDelete,
            fg_color="white",
            bg_color=self.selected_color.delete,
            bg_pressed_color=self.selected_color.delete_alt,
        )


class Preview(QWidget, Preview_ui.Ui_Form):
    def __init__(self, cls, html: str):
        super().__init__()
        self.setupUi(self)
        self.selected_color = cls.selected_color
        self.webview.setHtml(html)
        self.setupPreviewButtons(cls, html)

    def setupPreviewButtons(self, cls, html: str):
        modify_button(
            self.btnHome,
            fg_color="white",
            bg_color=self.selected_color.accent,
            bg_pressed_color=self.selected_color.accent_alt,
        )
        modify_button(
            self.btnSavePDF,
            fg_color="white",
            bg_color=self.selected_color.accent,
            bg_pressed_color=self.selected_color.accent_alt,
        )
        self.btnSavePDF.clicked.connect(lambda: save_pdf(cls, self.btnSavePDF, html))
        self.btnHome.clicked.connect(lambda: cls.switchPage(setPage(cls)))


class ProjectManager(QWidget, Projects_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.selected_color = cls.selected_color
        self.loadProjects(cls)
        self.btnNew.clicked.connect(lambda: self.newOrAddProject(cls))

    def loadProjects(self, cls) -> None:
        projects = ProjectModel.get_all(cls.db)
        for project in projects:
            widget = Project(cls.db, self.selected_color, project.project_id)
            self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
            widget.btnEdit.clicked.connect(
                lambda _, p=project: self.newOrAddProject(cls, p)
            )
            widget.btnDelete.clicked.connect(lambda _, w=widget: self.deleteProject(w))
            widget.btnPreview.clicked.connect(
                lambda _, p=project: self.previewProject(cls, p)
            )

    def newOrAddProject(self, cls, project: ProjectModel | None = None) -> None:
        widget = new_project.setPage(cls, project)
        cls.switchPage(widget)

    def previewProject(self, cls, project: ProjectModel) -> None:
        products = ProductModel.get(cls.db, project_id=project.project_id)
        pretty_total = (
            project.total
            if not str(project.total).endswith(".0")
            else int(project.total)
        )
        html = render_template(
            f"{Path.html_tpls}/{project.template}",
            project_name=project.name,
            items=products,
            total=pretty_total,
        )
        cls.switchPage(Preview(cls, html))

    def deleteProject(self, widget: Project) -> None:
        widget.db_object.delete()
        widget.deleteLater()
        self.verticalLayout.removeWidget(widget)


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.projects["title"])
    cls.lblDescription.setText(Pages.projects["description"])
    widget = ProjectManager(cls)
    return widget
