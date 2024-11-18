import os


class Path:
    current = os.path.dirname(os.path.realpath(__file__))
    templates = f"{current}/qss/templates"
