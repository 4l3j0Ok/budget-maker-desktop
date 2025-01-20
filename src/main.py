from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QPropertyAnimation, QEvent, QTranslator, QLibraryInfo
from controllers import products, projects
from views.ui.MainWindow_ui import Ui_MainWindow as MainWindow
from views.ui.sizes import Size
from views.ui.colors import Light, Dark
from models.database import Database
from utils import load_stylesheet_tpl, modify_button
from config import Features
import sys


class MainWindow(QMainWindow, MainWindow):
    def __init__(self, dark_mode: bool = False) -> None:
        super().__init__()
        # UI Setup
        self.setupUi(self)
        self.setupNavbar()
        self.dark_mode = dark_mode
        self.current_page = None
        ## Window
        self.setMinimumWidth(Size.app_min_width)
        self.setMinimumHeight(Size.app_min_height)
        ## Navbar
        self.setupButtons()
        self.btnPage = {
            "btnProjects": projects.setPage,
            "btnProducts": products.setPage,
        }
        # Database
        self.db = Database()
        self.switchPage(self.btnPage["btnProjects"](self))
        return

    def setupNavbar(self) -> None:
        self.frNavbar.setMaximumWidth(Size.navbar_base_width)
        self.btnMenu.clicked.connect(self.toggleMenu)
        if not Features.projects:
            self.btnProjects.hide()
        if not Features.products:
            self.btnProducts.hide()
        return

    def toggleMenu(self) -> None:
        current_width = self.frNavbar.maximumWidth()
        new_width = (
            Size.navbar_max_width
            if current_width == Size.navbar_base_width
            else Size.navbar_base_width
        )
        self.animation = QPropertyAnimation(self.frNavbar, b"maximumWidth")
        self.animation.setDuration(100)
        self.animation.setStartValue(current_width)
        self.animation.setEndValue(new_width)
        self.animation.start()
        return

    def setupButtons(self) -> None:
        buttons = self.frNavbar.findChildren(QPushButton)
        for button in buttons:
            modify_button(
                button,
                fg_color=Dark.button_text,
            ) if self.dark_mode else modify_button(button, fg_color=Light.button_text)
            button.installEventFilter(self)
            if button.objectName() != "btnMenu":
                button.clicked.connect(self.switchPage)
        return

    def switchPage(self, widget: QWidget = None, hide=False, hidden=False) -> None:
        if not widget:
            button = self.sender()
            widget = self.btnPage[button.objectName()](self)
        self.current_page = widget
        layout = self.frContent.layout()
        if layout.count() > 0:
            current_widget = layout.itemAt(0).widget()
            for i in range(layout.count()):
                if hide:
                    if layout.itemAt(i).widget() == current_widget:
                        layout.itemAt(i).widget().hide()
                        continue
                if layout.itemAt(i).widget() != widget:
                    layout.itemAt(i).widget().deleteLater()
        self.frContent.layout().addWidget(widget) if not hidden else widget.show()
        return

    def eventFilter(self, obj, event) -> bool:
        selected_color = Light if not self.dark_mode else Dark
        if event.type() == QEvent.Type.HoverEnter:
            modify_button(
                obj,
                fg_color=selected_color.button_text_alt,
            )
        elif event.type() == QEvent.Type.HoverLeave:
            modify_button(
                obj,
                fg_color=selected_color.button_text,
            )
        return super().eventFilter(obj, event)


def init_translator(app: QApplication) -> None:
    translator = QTranslator(app)
    translations = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_translator(app)
    app.setStyle("Fusion")
    dark_mode = False
    load_stylesheet_tpl(app, dark_mode=dark_mode)
    window = MainWindow(dark_mode=dark_mode)
    window.show()
    app.exec()
