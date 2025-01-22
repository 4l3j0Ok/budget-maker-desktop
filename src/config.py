import os
import dotenv

dotenv.load_dotenv()


class Features:
    projects = True
    products = False
    config = False


class Environment:
    dev_mode = os.getenv("DEV_MODE", "False").lower() == "true"


class Path:
    current = os.path.dirname(os.path.realpath(__file__))
    qss_tpls = f"{current}/views/qss/templates"
    html_tpls = f"{current}/views/html/templates"


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


class Database:
    name = "data.db"


class Project:
    default_template = "formal-negro.html.tpl"
