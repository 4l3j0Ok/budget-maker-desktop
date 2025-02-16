import os
import environment


class Features:
    projects = True
    products = False
    config = False


class Path:
    current = os.path.dirname(os.path.realpath(__file__))
    qss_tpls = (
        f"{current}/views/qss/templates"
        if environment.DEV_MODE
        else f"{current}/qss/templates"
    )
    html_tpls = (
        f"{current}/views/html/templates"
        if environment.DEV_MODE
        else f"{current}/html/templates"
    )
    settings = "settings.json"


class Pages:
    home = dict(
        title="Inicio",
        description="Página de inicio",
    )
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
    settings = dict(
        title="Configuración",
        description="Configura la aplicación a tu gusto",
    )
    about = dict(
        title="Acerca de",
        description="Información sobre la aplicación",
    )


class Database:
    name = "data.db"


class Project:
    default_template = "formal-negro.html.tpl"
