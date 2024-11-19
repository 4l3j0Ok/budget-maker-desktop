from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QSizePolicy,
)
from PySide6.QtGui import QIcon, QPainter
from PySide6.QtCore import QPropertyAnimation
from ui.MainWindow_ui import Ui_MainWindow as MainWindow
from ui.sizes import Size
from ui.colors import Light, Dark
from forms.new_project import NewProject
from config import Pages
from utils import load_stylesheet_tpl
import sys


class MainWindow(QMainWindow, MainWindow):
    def __init__(self, dark_mode=False) -> None:
        super().__init__()
        self.setupUi(self)
        self.setupNavbar()
        self.darkMode: bool = dark_mode
        self.current_page: QWidget = None
        self.setMinimumWidth(Size.app_min_width)
        self.setMinimumHeight(Size.app_min_height)
        self.setupButtons()
        return

    def setupNavbar(self) -> None:
        self.frNavbar.setMaximumWidth(Size.navbar_base_width)
        self.btnMenu.clicked.connect(self.toggleMenu)
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
            self.setButtonColor(
                Dark.button, button
            ) if self.darkMode else self.setButtonColor(Light.button_text, button)
            button.installEventFilter(self)
            if button.objectName() != "btnMenu":
                button.clicked.connect(self.switchPage)
        return

    def setButtonColor(self, color, button) -> None:
        icon = button.icon()
        current_size = button.iconSize()
        pixmap = icon.pixmap(current_size)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        button.setIcon(QIcon(pixmap))
        return

    def switchPage(self) -> None:
        button = self.sender()
        if button.objectName() == "btnProjects":
            # Establecer el título y la descripción de la página.
            self.lblTitle.setText(Pages.new_project["title"])
            self.lblDescription.setText(Pages.new_project["description"])
            # Reemplazar el contenido de frContent
            if isinstance(self.current_page, NewProject):
                return
            widget = NewProject(self.frContent)
            self.current_page = widget
            if self.frContent.layout().count() > 0:
                self.frContent.layout().removeItem(self.frContent.layout().itemAt(0))
            self.frContent.layout().addWidget(widget)
        return

    def eventFilter(self, obj, event) -> bool:
        selected_color = Light if not dark_mode else Dark
        if event.type() == event.Type.HoverEnter:
            self.setButtonColor(selected_color.button_text_alt, obj)
        elif event.type() == event.Type.HoverLeave:
            self.setButtonColor(selected_color.button_text, obj)
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    print(sys.argv)
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dark_mode = False
    load_stylesheet_tpl(app, dark_mode=dark_mode)
    window = MainWindow(dark_mode=dark_mode)
    window.show()
    app.exec()
