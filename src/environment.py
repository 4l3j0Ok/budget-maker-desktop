import os
import dotenv

dotenv.load_dotenv()


DEV_MODE = os.getenv("DEV_MODE", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
APP_VERSION = os.getenv("APP_VERSION", "0.0.1")
