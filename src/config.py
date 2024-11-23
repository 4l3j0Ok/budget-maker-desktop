import os


class Path:
    current = os.path.dirname(os.path.realpath(__file__))
    templates = f"{current}/views/qss/templates"


class Pages:
    new_project = dict(
        title="Nuevo Proyecto",
        description="Introduce los datos del nuevo proyecto",
    )
