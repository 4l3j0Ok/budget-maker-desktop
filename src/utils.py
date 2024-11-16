from PySide6.QtWidgets import QApplication
from ui import colors


def load_stylesheet(
    app: QApplication,
    mode: str = "light",
    qss_path: str = "src/qss",
) -> None:
    style_file = f"{qss_path}/{mode}.qss"
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {style_file}")


def load_stylesheet_tpl(
    app: QApplication,
    mode: str = "light",
    qss_path: str = "src/qss/templates",
) -> None:
    style_file = f"{qss_path}/{mode}.qss.tpl"
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            selected_color = colors.Light if mode == "light" else colors.Dark
            for color in selected_color:
                stylesheet = stylesheet.replace(f"${color.name}", color.value)
            app.setStyleSheet(stylesheet)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {style_file}")
