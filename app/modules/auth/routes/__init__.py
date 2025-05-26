from flask import Blueprint

auth_bp = Blueprint("auth", import_name=__name__, template_folder="../templates", url_prefix="/auth") # template resolution to make sure each module is self-contained


from ..routes.login import login
from ..routes.register import register
from ..routes.logout import logout

auth_bp.add_url_rule(
    rule="/login",
    endpoint="login",
    view_func=login,
    methods=["GET", "POST"]
)


auth_bp.add_url_rule(
    rule="/register",
    endpoint="register",
    view_func=register,
    methods=["GET", "POST"]
)


auth_bp.add_url_rule(
    rule="/logout",
    endpoint="logout",
    view_func=logout,
    methods=["GET"]
)