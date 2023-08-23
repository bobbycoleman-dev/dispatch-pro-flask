from flask_app.models.distribution_center import DistributionCenter
from flask import Blueprint, redirect, render_template, request
from flask_app.forms.register import RegisterForm
from flask_app.models.user import User
from flask_app.models.role import Role
from flask_app.extensions import db

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.get("/user_settings")
def go_to_users_settings():
    """Navigate to User Settings to view all and add a User"""
    dcs = DistributionCenter.query.all()
    users = User.query.all()
    form = RegisterForm()
    roles = Role().roles
    form.dc_id.choices = [
        (int(dc.id), dc.nickname) for dc in DistributionCenter.query.all()
    ]
    return render_template(
        "/users/user_settings.html", users=users, dcs=dcs, form=form, roles=roles
    )
