import os
import shutil
import sys
import zipfile
import requests
from PySide6.QtWidgets import (
    QApplication,
    QProgressBar,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
from PySide6.QtGui import QIcon
from logger import get_logger
import config
import resources_rc


class Updater(QWidget):
    def __init__(self, app_path: str):
        super().__init__()
        self.initUI()
        self.logger = get_logger("updater")
        self.logger.info("Iniciando actualización")
        self.unzipped = 0
        self.downloaded = 0
        self.url = self.getReleaseDownloadUrl()
        self.response = requests.get(self.url, stream=True)
        self.app_path = app_path
        self.zip_file = os.path.join(self.app_path, config.Application.artifact_name)
        self.total_length = int(self.response.headers.get("content-length", 0))
        self.block_size = 1024
        self.startUpdate()

    def initUI(self):
        self.setWindowTitle(f"Actualizando {config.Application.name}")
        icon = QIcon(":/icons/views/assets/icon.png")
        self.setWindowIcon(icon)
        self.setFixedSize(300, 100)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.layout.addWidget(QLabel("Actualizando aplicación..."))
        self.layout.addWidget(self.progress_bar)
        self.progress_bar.setValue(0)
        self.show()

    def startUpdate(self):
        success, result = self.downloadZip(clear_dest=True)
        if not success:
            self.handleError(result)
            return
        success, result = self.unzip()
        if not success:
            self.handleError(result)
            return
        self.handleSuccess()

    def downloadZip(self, clear_dest=True):
        try:
            if clear_dest:
                self.clearDestinationDirectory()
            self.logger.info(f"Descargando actualización desde {self.url}")
            self.logger.info(f"Guardando archivo en {self.zip_file}")
            self.saveZipFile()
            return True, config.Application.artifact_name
        except Exception as ex:
            self.logger.exception(ex)
            return False, f"Error al descargar la actualización: {ex}"

    def clearDestinationDirectory(self):
        exclude = [config.Path.settings, config.Path.database, config.Path.log]
        for file in os.listdir(self.app_path):
            if file not in exclude:
                shutil.rmtree(os.path.join(self.app_path, file), ignore_errors=True)
        os.makedirs(self.app_path, exist_ok=True)

    def saveZipFile(self):
        with open(self.zip_file, "wb") as file:
            for data in self.response.iter_content(self.block_size):
                file.write(data)
                self.updateProgress(len(data))

    def updateProgress(self, data_length):
        self.downloaded += data_length
        progress = int((self.downloaded / self.total_length) * 50)
        self.progress_bar.setValue(progress)
        QApplication.processEvents()

    def unzip(self):
        try:
            with zipfile.ZipFile(self.zip_file, "r") as zip_ref:
                total_files = len(zip_ref.infolist())
                for i, file in enumerate(zip_ref.infolist(), 1):
                    zip_ref.extract(file, self.app_path)
                    self.updateUnzipProgress(total_files)
            return True, "Descompresión completada"
        except Exception as ex:
            self.logger.exception(ex)
            return False, f"Error al descomprimir el archivo: {ex}"

    def updateUnzipProgress(self, total_files):
        self.unzipped += 1
        progress = 50 + int((self.unzipped / total_files) * 50)
        self.progress_bar.setValue(progress)
        QApplication.processEvents()

    @staticmethod
    def getLatestVersion(logger):
        try:
            response = requests.get(config.Application.release_api).json()
            logger.debug(f"Última versión: {response['tag_name']}")
            return response["tag_name"]
        except requests.exceptions.RequestException as e:
            logger.exception(e)
            return ""

    def getReleaseDownloadUrl(self):
        return config.Application.release_download_url.format(
            version=self.getLatestVersion(self.logger)
        )

    def handleError(self, message):
        self.logger.error(message)
        QMessageBox.critical(self, "Error", message)
        QApplication.processEvents()
        self.closeApp()

    def handleSuccess(self):
        self.logger.info("Actualización descargada y descomprimida correctamente")
        QMessageBox.information(self, "Éxito", "Actualización completada correctamente")
        self.closeApp()

    def closeApp(self):
        QApplication.processEvents()
        sys.exit()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    default_app_path = (
        config.Path.current() if not config.environment.DEV_MODE else "./tests"
    )
    updater = Updater(sys.argv[1]) if len(sys.argv) > 1 else Updater(default_app_path)
    sys.exit(app.exec())
