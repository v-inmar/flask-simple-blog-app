from flask import Blueprint

user_bp = Blueprint("user", import_name=__name__, template_folder="../templates", url_prefix="/users")

from ..routes.profile import profile

user_bp.add_url_rule(
    rule="/<pid>",
    endpoint="profile",
    view_func=profile,
    methods=["GET"]
)