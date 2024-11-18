from PySide6.QtWidgets import QApplication
from ui import colors
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
