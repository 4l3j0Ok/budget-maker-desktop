from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtGui import QIcon, QPainter, QPageLayout, QPageSize
from PySide6.QtCore import QMarginsF
from PySide6.QtWebEngineWidgets import QWebEngineView
from logger import logger
from views.ui import colors
from config import Path
from jinja2 import Template
import os


def load_stylesheet(
    app: QApplication,
    dark_mode: bool = False,
) -> None:
    style_file = (
        f"{Path.qss_tpls}/dark.qss.tpl"
        if dark_mode
        else f"{Path.qss_tpls}/light.qss.tpl"
    )
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except FileNotFoundError as fex:
        logger.exception(fex)
        logger.error(f"Archivo no encontrado: {style_file}")


def load_stylesheet_tpl(
    app: QApplication,
    dark_mode: bool = False,
) -> None:
    style_file = (
        f"{Path.qss_tpls}/light.qss.tpl"
        if not dark_mode
        else f"{Path.qss_tpls}/dark.qss.tpl"
    )
    try:
        with open(style_file) as file:
            stylesheet = file.read()
            selected_color = colors.Light if not dark_mode else colors.Dark
            for key, color in selected_color.__dict__.items():
                stylesheet = stylesheet.replace("${" + f"{key}" + "}", f"{color}")
            app.setStyleSheet(stylesheet)
    except FileNotFoundError as fex:
        logger.exception(fex)
        logger.error(f"Archivo no encontrado: {style_file}")


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


def get_template_list():
    return os.listdir(Path.html_tpls)


def render_template(
    template_file: str,
    **kwargs,
) -> str:
    with open(template_file) as file:
        template = Template(file.read())
        return template.render(**kwargs)


def create_pdf(html: str, output_file: str) -> tuple[bool, str]:
    try:
        webView = QWebEngineView()
        layout = QPageLayout(QPageSize.A4, QPageLayout.Portrait, QMarginsF(0, 0, 0, 0))

        def on_load_finished(success):
            if success:
                webView.page().printToPdf(output_file, layout)
            else:
                raise Exception("Failed to load HTML content")

        webView.loadFinished.connect(on_load_finished)
        webView.setHtml(html)

        return True, output_file
    except Exception as ex:
        logger.exception(ex)
        return False, str(ex)


def save_pdf(btnSave, html: str) -> None:
    file_path, _ = QFileDialog.getSaveFileName(
        caption="Guardar PDF",
        dir="",
        filter="PDF Files (*.pdf)",
    )
    if file_path:
        create_pdf(html, file_path)
        modify_button(
            btnSave,
            fg_color="white",
            bg_color=colors.Light.selected,
            bg_pressed_color=colors.Light.selected_alt,
        )
