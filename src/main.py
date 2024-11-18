from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon, QPainter
from PySide6.QtCore import QPropertyAnimation
from ui import MainWindow_ui as MainWindow
from ui.sizes import Size
from utils import load_stylesheet_tpl
from ui.colors import Light, Dark
import sys


class MainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)
        self.setupNavbar()
        self.setMinimumWidth(Size.app_min_width)
        self.setMinimumHeight(Size.app_min_height)
        self.setupButtons()

    def setupNavbar(self):
        self.frNavbar.setMaximumWidth(Size.navbar_base_width)
        self.btnMenu.clicked.connect(self.toggleMenu)

    def toggleMenu(self):
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

    def setupButtons(self):
        buttons = self.frNavbar.findChildren(QPushButton)
        for button in buttons:
            self.setButtonColor(
                Dark.button, button
            ) if dark_mode else self.setButtonColor(Light.button, button)
            button.installEventFilter(self)
            if button.objectName() != "btnMenu":
                button.clicked.connect(self.switchPage)

    def setButtonColor(self, color, button):
        icon = button.icon()
        current_size = button.iconSize()
        pixmap = icon.pixmap(current_size)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        button.setIcon(QIcon(pixmap))
        return

    def switchPage(self):
        # Acá hay que renderizar el widget correspondiente.
        pass

    def eventFilter(self, obj, event):
        selected_color = Light if not dark_mode else Dark
        if event.type() == event.Type.HoverEnter:
            self.setButtonColor(selected_color.button_hover, obj)
        elif event.type() == event.Type.HoverLeave:
            self.setButtonColor(selected_color.button, obj)
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
