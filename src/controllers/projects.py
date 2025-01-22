from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Projects_ui, Project_ui
from controllers import new_project
from models.projects import ProjectModel
from views.ui import colors
from config import Pages
from utils import modify_button


class Project(QWidget, Project_ui.Ui_Element):
    def __init__(self, db, project_id: int):
        super().__init__()
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setupProjectBox()
        self.setupButtons()
        self.db_object = ProjectModel.get(db, project_id)
        self.lblProjectName.setText(self.db_object.name)

    def setupProjectBox(self):
        style_sheet = f"""
            QFrame {{
                background-color: {colors.Light.card_background};
                border-radius: 5px;
                border: 1px solid {colors.Light.card_border};
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
            bg_color=colors.Light.accent,
            bg_pressed_color=colors.Light.accent_alt,
        )
        modify_button(
            self.btnPreview,
            fg_color="white",
            bg_color=colors.Light.accent,
            bg_pressed_color=colors.Light.accent_alt,
        )
        modify_button(
            self.btnDelete,
            fg_color="white",
            bg_color=colors.Light.delete,
            bg_pressed_color=colors.Light.delete_alt,
        )


class ProjectManager(QWidget, Projects_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.loadProjects(cls)
        self.btnNew.clicked.connect(lambda: self.NewOrAddProject(cls))

    def loadProjects(self, cls) -> None:
        projects = ProjectModel.get_all(cls.db)
        for project in projects:
            widget = Project(cls.db, project.project_id)
            self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
            widget.btnEdit.clicked.connect(
                lambda _, p=project: self.NewOrAddProject(cls, p)
            )
            widget.btnDelete.clicked.connect(lambda _, w=widget: self.deleteProject(w))

    def NewOrAddProject(self, cls, project: ProjectModel | None = None) -> None:
        widget = new_project.setPage(cls, project)
        cls.switchPage(widget)

    def previewProject(self, project: ProjectModel) -> None:
        pass

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
