from enum import Enum
import os


class Path(Enum):
    current = os.path.dirname(os.path.realpath(__file__))
    templates = f"{current}/qss/templates"
