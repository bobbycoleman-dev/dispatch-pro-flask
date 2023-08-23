from flask import Blueprint, render_template, redirect


bp = Blueprint("main", __name__)


@bp.get("/")
def redirect_user():
    return redirect("/auth/login")
