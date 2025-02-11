import os
import dotenv

dotenv.load_dotenv()

"""
Este archivo se encarga de cargar las variables de entorno en base al archivo .env.
En build time, las variables serán reemplazadas por los valores correspondientes.
Para más info acerca de este funcionamiento, revisa el archivo python-app.yml en .github/workflows.
"""

DEV_MODE = os.getenv("DEV_MODE", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
APP_VERSION = os.getenv("APP_VERSION", "0.0.1")
