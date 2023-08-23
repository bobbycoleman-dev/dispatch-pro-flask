from flask import Blueprint, flash, render_template, redirect, request, session
from flask_login import current_user
from flask_app.models.role import Role
from flask_app.models.dc_region import DCRegion

bp = Blueprint("navigation", __name__)


@bp.route("/settings")
def go_to_settings():
    roles = Role().roles
    regions = DCRegion().south
    current_user.region = (
        "South" if current_user.user_dc.state in regions else "Northeast"
    )
    return render_template("/account_settings.html", roles=roles)
