import os


class Path:
    current = os.path.dirname(os.path.realpath(__file__))
    templates = f"{current}/views/qss/templates"


class Pages:
    projects = dict(
        title="Proyectos",
        description="Todos tus proyectos creados",
    )
    new_project = dict(
        title="Nuevo Proyecto",
        description="Introduce los datos del nuevo proyecto",
    )
    products = dict(
        title="Productos",
        description="Añade productos a tu proyecto de forma sencilla",
    )
