from flask import Blueprint

post_bp = Blueprint(name="post", import_name=__name__, template_folder="../templates", url_prefix="/posts")

from ..routes.create import create
from ..routes.read import read
from ..routes.update import update
from ..routes.delete import delete

post_bp.add_url_rule(
    rule="/create",
    endpoint="create",
    view_func=create,
    methods=["GET", "POST"]
)


post_bp.add_url_rule(
    rule="/<pid>",
    endpoint="read",
    view_func=read,
    methods=["GET"]
)


post_bp.add_url_rule(
    rule="/<pid>/update",
    endpoint="update",
    view_func=update,
    methods=["GET", "POST"]
)

post_bp.add_url_rule(
    rule="/<pid>/delete",
    endpoint="delete",
    view_func=delete,
    methods=["GET"]
)
