from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPainter, QPageLayout, QPageSize
from PySide6.QtCore import QMarginsF
from PySide6.QtWebEngineWidgets import QWebEngineView
from logger import logger
from config import Path
from jinja2 import Template
import os


def load_stylesheet_tpl(
    cls,
) -> None:
    try:
        with open(cls.selected_color.template_file) as file:
            stylesheet = file.read()
            for key, color in cls.selected_color.__dict__.items():
                stylesheet = stylesheet.replace("${" + f"{key}" + "}", f"{color}")
            cls.setStyleSheet(stylesheet)
    except FileNotFoundError as fex:
        logger.exception(fex)
        logger.error(f"Archivo no encontrado: {cls.selected_color.template_file}")


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
                raise Exception("Error al cargar la página.")

        webView.loadFinished.connect(on_load_finished)
        webView.setHtml(html)

        return True, output_file
    except Exception as ex:
        logger.exception(ex)
        return False, str(ex)


def save_pdf(cls, btnSave, html: str, default_filename: str = "") -> None:
    file_path = (
        cls.settings.default_export_path + f"/{default_filename}.pdf"
        if cls.settings.save_without_ask
        and os.path.exists(cls.settings.default_export_path)
        else QFileDialog.getSaveFileName(
            caption="Guardar PDF",
            dir=cls.settings.default_export_path + f"/{default_filename}.pdf",
            filter="PDF Files (*.pdf)",
        )[0]
    )
    if file_path:
        success, result = create_pdf(html, file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information if success else QMessageBox.Critical)
        msg_box.setWindowTitle("Exportar PDF")
        msg_box.setText(f"PDF exportado con éxito en {result}" if success else result)
        msg_box.setWindowIcon(cls.windowIcon())
        msg_box.exec_()
        modify_button(
            btnSave,
            fg_color=cls.selected_color.button_text_alt,
            bg_color=cls.selected_color.selected
            if success
            else cls.selected_color.delete,
            bg_pressed_color=cls.selected_color.selected_alt
            if success
            else cls.selected_color.delete_alt,
        )
