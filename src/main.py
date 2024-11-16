from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon, QPainter
from ui import MainWindow_ui as MainWindow
from ui.config import Size
from utils import load_stylesheet_tpl
import sys


class MainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)
        self.setupNavbar()
        self.setMinimumWidth(Size.app_min_width.value)
        self.setMinimumHeight(Size.app_min_height.value)
        self.setButtonsColor("white") if dark_mode else self.setButtonsColor("#333")

    def setupNavbar(self):
        self.frNavbar.setMaximumWidth(Size.navbar_base_width.value)
        self.btnMenu.clicked.connect(self.toggleMenu)

    def toggleMenu(self):
        self.frNavbar.setMaximumWidth(
            Size.navbar_max_width.value
            if self.frNavbar.maximumWidth() == Size.navbar_base_width.value
            else Size.navbar_base_width.value
        )

    def setButtonsColor(self, color):
        buttons = self.frNavbar.findChildren(QPushButton)
        for button in buttons:
            button: QPushButton
            current_style_sheet = button.styleSheet()
            button.setStyleSheet(f"{current_style_sheet}; color: {color}")
            # Change icon color
            icon = button.icon()
            current_size = button.iconSize()
            pixmap = icon.pixmap(current_size)
            painter = QPainter(pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            painter.fillRect(pixmap.rect(), color)
            painter.end()
            button.setIcon(QIcon(pixmap))


if __name__ == "__main__":
    print(sys.argv)
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dark_mode = True
    load_stylesheet_tpl(app, mode="dark" if dark_mode else "light")
    window = MainWindow(dark_mode=dark_mode)
    window.show()
    app.exec()
