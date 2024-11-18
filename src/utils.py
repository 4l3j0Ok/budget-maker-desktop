from PySide6.QtWidgets import QApplication
from ui import colors
from config import Path


def load_stylesheet(
    app: QApplication,
    dark_mode: bool = False,
) -> None:
    style_file = (
        f"{Path.templates.value}/dark.qss.tpl"
        if dark_mode
        else f"{Path.templates.value}/light.qss.tpl"
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
        f"{Path.templates.value}/light.qss.tpl"
        if not dark_mode
        else f"{Path.templates.value}/dark.qss.tpl"
    )
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            selected_color = colors.Light if not dark_mode else colors.Dark
            for color in selected_color:
                stylesheet = stylesheet.replace(
                    "${" + f"{color.name}" + "}", f"{color.value}"
                )
            app.setStyleSheet(stylesheet)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {style_file}")
