from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QPainter
from views.ui import colors
from config import Path


def load_stylesheet(
    app: QApplication,
    dark_mode: bool = False,
) -> None:
    style_file = (
        f"{Path.templates}/dark.qss.tpl"
        if dark_mode
        else f"{Path.templates}/light.qss.tpl"
    )
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {style_file}")


def load_stylesheet_tpl(
    app: QApplication,
    dark_mode: bool = False,
) -> None:
    style_file = (
        f"{Path.templates}/light.qss.tpl"
        if not dark_mode
        else f"{Path.templates}/dark.qss.tpl"
    )
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            selected_color = colors.Light if not dark_mode else colors.Dark
            for key, color in selected_color.__dict__.items():
                stylesheet = stylesheet.replace("${" + f"{key}" + "}", f"{color}")
            app.setStyleSheet(stylesheet)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {style_file}")


def modify_button(
    button,
    fg_color: str = None,
    bg_color: str = None,
    bg_pressed_color: str = None,
    icon: str = None,
) -> None:
    if icon:
        icon = QIcon(icon)
        button.setIcon(icon)
    if bg_color:
        current_style = button.styleSheet()
        current_style += f"""
        QPushButton {{
            background-color: {bg_color};
        }}"""
        button.setStyleSheet(current_style)
    if bg_pressed_color:
        current_style = button.styleSheet()
        current_style += f"""
        QPushButton:pressed {{
            background-color: {bg_pressed_color};
        }}"""
        button.setStyleSheet(current_style)
    if fg_color:
        current_size = button.iconSize()
        icon = button.icon()
        pixmap = icon.pixmap(current_size)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), fg_color)
        painter.end()
        button.setIcon(QIcon(pixmap))
    return
