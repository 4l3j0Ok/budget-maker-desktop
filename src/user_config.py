import os
import json
from config import Path
from logger import logger


class UserConfig:
    dark_mode: bool
    default_export_path: str

    def __init__(self, dark_mode: bool = False, default_export_path: str = ""):
        self.dark_mode = dark_mode
        self.default_export_path = default_export_path

    def save(self):
        with open(Path.user_config, "w") as f:
            logger.info("Creando archivo de configuración del usuario.")
            json.dump(self.__dict__, f, indent=4)

    @staticmethod
    def load():
        if not os.path.exists(Path.user_config):
            logger.warning("Archivo de configuración del usuario no encontrado.")
            user_config = UserConfig()
            user_config.save()
            return user_config
        with open(Path.user_config, "r") as f:
            data = json.load(f)
            return UserConfig(**data)
