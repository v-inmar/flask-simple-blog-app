from flask import Blueprint

dashboard_bp = Blueprint("dashboard", import_name=__name__, template_folder="../templates") # template resolution to make sure each module is self-contained

from app.modules.dashboard.routes.get_dashboard import get_dashboard


# List of routes you want to add to the dashboard
url_rules = ["/", "/home", "/index", "/dashboard"]


for url_rule in url_rules:
    dashboard_bp.add_url_rule(
        rule=url_rule,
        endpoint="dashboard",
        view_func=get_dashboard,
        methods=["GET"]
    )
