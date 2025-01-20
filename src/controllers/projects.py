from PySide6.QtWidgets import QWidget, QSizePolicy
from views.ui import Projects_ui, Project_ui
from controllers import new_project
from models.projects import Project as ProjectModel
from views.ui import colors
from config import Pages
from utils import modify_button


class Project(QWidget, Project_ui.Ui_Element):
    def __init__(self, project_db: ProjectModel):
        super().__init__()
        self.setupUi(self)
        self.project_db = project_db
        self.lblProjectName.setText(project_db.name)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setupProjectBox()
        self.setupButtons()

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


class Projects(QWidget, Projects_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.loadProjects(cls)
        self.btnNew.clicked.connect(lambda: self.onBtnNewOrAddClicked(cls))

    def loadProjects(self, cls) -> None:
        projects = ProjectModel.get_all(cls.db)
        for project in projects:
            widget = Project(project)
            self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget)
            widget.btnEdit.clicked.connect(
                lambda: self.onBtnNewOrAddClicked(cls, project)
            )
        return

    def onBtnNewOrAddClicked(self, cls, project: ProjectModel | None = None) -> None:
        widget = new_project.setPage(cls, project)
        cls.switchPage(widget)
        return


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.projects["title"])
    cls.lblDescription.setText(Pages.projects["description"])
    widget = Projects(cls)
    return widget
