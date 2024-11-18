from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon, QPainter
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
        self.setMinimumWidth(Size.app_min_width.value)
        self.setMinimumHeight(Size.app_min_height.value)
        self.setButtonsColor(Dark.button.value) if dark_mode else self.setButtonsColor(
            Light.button.value
        )

    def setupNavbar(self):
        self.frNavbar.setMaximumWidth(Size.navbar_base_width.value)
        self.btnMenu.clicked.connect(self.toggleMenu)

    def toggleMenu(self):
        self.frNavbar.setMaximumWidth(
            Size.navbar_max_width.value
            if self.frNavbar.maximumWidth() == Size.navbar_base_width.value
            else Size.navbar_base_width.value
        )

    def setButtonsColor(self, color, button=None):
        if button:
            icon = button.icon()
            current_size = button.iconSize()
            pixmap = icon.pixmap(current_size)
            painter = QPainter(pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            painter.fillRect(pixmap.rect(), color)
            painter.end()
            button.setIcon(QIcon(pixmap))
            return
        buttons = self.frNavbar.findChildren(QPushButton)
        for button in buttons:
            button: QPushButton
            # conectar evento de focus a la función de cambio de color
            button.installEventFilter(self)
            icon = button.icon()
            current_size = button.iconSize()
            pixmap = icon.pixmap(current_size)
            painter = QPainter(pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            painter.fillRect(pixmap.rect(), color)
            painter.end()
            button.setIcon(QIcon(pixmap))

    def eventFilter(self, obj, event):
        selected_color = Light if not dark_mode else Dark
        if event.type() == event.Type.HoverEnter:
            self.setButtonsColor(selected_color.button_hover.value, button=obj)
        elif event.type() == event.Type.HoverLeave:
            self.setButtonsColor(selected_color.button.value, button=obj)
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
