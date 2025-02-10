import os
import json
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog
from views.ui import Settings_ui
from config import Path, Pages
from logger import logger
from views.ui import colors
from utils import load_stylesheet_tpl


class SettingsModel:
    dark_mode: bool
    default_export_path: str

    def __init__(self, dark_mode: bool = False, default_export_path: str = ""):
        self.dark_mode = dark_mode
        self.default_export_path = default_export_path

    def save(self):
        with open(Path.settings, "w") as f:
            logger.info("Guardando configuración del usuario.")
            logger.debug(f"Configuración: {self.__dict__}")
            json.dump(self.__dict__, f, indent=4)

    @staticmethod
    def load() -> "SettingsModel":
        if not os.path.exists(Path.settings):
            logger.warning("Archivo de configuración del usuario no encontrado.")
            settings = SettingsModel()
            settings.save()
            return settings
        with open(Path.settings, "r") as f:
            data = json.load(f)
            return SettingsModel(**data)


class Settings(QWidget, Settings_ui.Ui_Form):
    def __init__(self, cls):
        super().__init__()
        self.setupUi(self)
        self.settings = cls.settings
        self.cbDarkMode.setChecked(self.settings.dark_mode)
        self.lePDFExportPath.setText(self.settings.default_export_path)
        self.btnSearch.clicked.connect(self.selectPath)
        self.cbDarkMode.checkStateChanged.connect(lambda: self.toggleDarkMode(cls))
        self.lePDFExportPath.textChanged.connect(self.updatePath)

    def toggleDarkMode(self, cls):
        cls.selected_color = (
            colors.Dark if self.cbDarkMode.isChecked() else colors.Light
        )
        load_stylesheet_tpl(cls)
        self.settings.dark_mode = self.cbDarkMode.isChecked()
        self.settings.save()
        cls.setupButtons()

    def selectPath(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Selecciona la carpeta de exportación",
            self.settings.default_export_path,
        )
        if path:
            self.lePDFExportPath.setText(path)

    def updatePath(self):
        self.settings.default_export_path = self.lePDFExportPath.text()
        self.settings.save()


def setPage(cls) -> None:
    # Establecer el título y la descripción de la página.
    cls.lblTitle.setText(Pages.settings["title"])
    cls.lblDescription.setText(Pages.settings["description"])
    widget = Settings(cls)
    return widget
