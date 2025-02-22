import os
import environment


class Application:
    name = "Budget Maker Desktop"
    version = environment.APP_VERSION
    dev_mode = environment.DEV_MODE
    log_level = environment.LOG_LEVEL
    log_name = "application"
    artifact_name = "budget-maker-desktop.zip"
    release_api = (
        "https://api.github.com/repos/4l3j0Ok/budget-maker-desktop/releases/latest"
    )
    release_download_url = f"https://github.com/4l3j0Ok/budget-maker-desktop/releases/download/{{version}}/{artifact_name}"


class Features:
    projects = True
    products = False
    config = False


class Path:
    current = os.path.dirname(os.path.realpath(__file__))
    qss_tpls = (
        f"{current}/views/qss/templates"
        if Application.dev_mode
        else f"{current}/_internal/qss/templates"
    )
    html_tpls = (
        f"{current}/views/html/templates"
        if Application.dev_mode
        else f"{current}/_internal/html/templates"
    )
    settings = "settings.json"
    database = "data.db"
    log = f"{current}/logs/{Application.log_name}.log"
    updater_exe = f"{current}/updater.exe"


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


class Project:
    default_template = "formal-negro.html.tpl"
