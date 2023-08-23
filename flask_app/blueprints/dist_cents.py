from flask_app.models.distribution_center import DistributionCenter
from flask_app.models.user import User
from flask_app.forms.dist_cent import DistributionCenterForm
from sqlalchemy import func
from flask_app.extensions import db

from flask import Blueprint, redirect, render_template, request

bp = Blueprint("dist_cents", __name__, url_prefix="/dcs")


@bp.get("/dc_settings")
def go_to_dc_settings():
    """Render the DC Settings Page"""
    dcs = DistributionCenter.query.all()
    form = DistributionCenterForm()
    return render_template("/dcs/dc_settings.html", dcs=dcs, form=form)


@bp.route("/create", methods=["GET", "POST"])
def create_dc():
    """Process the form to create a DC"""
    form = DistributionCenterForm()

    if form.validate_on_submit():
        nickname = request.form.get("nickname")
        street = request.form.get("street")
        city = request.form.get("city")
        state = request.form.get("state")
        zip_code = request.form.get("zip_code")

        new_dc = DistributionCenter(
            nickname=nickname, street=street, city=city, state=state, zip_code=zip_code
        )
        db.session.add(new_dc)
        db.session.commit()
        return redirect("/dcs/dc_settings")

    return render_template("/dcs/dc_settings.html", form=form)
