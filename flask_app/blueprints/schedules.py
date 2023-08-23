from flask import Blueprint, flash, render_template, redirect, request, session
from flask_app.forms.schedule import ScheduleForm
from flask_app.models.schedule import Schedule
from flask_app.models.truck import Truck
from flask_login import current_user
from flask_app.extensions import db
from flask_app.models.dc_region import DCRegion

bp = Blueprint("schedules", __name__)


@bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    trucks = Truck.query.filter(Truck.dc_id == current_user.dc_id)
    schedules = Schedule.query.filter(Truck.dc_id == current_user.dc_id)
    regions = DCRegion().south
    current_user.region = (
        "south" if current_user.user_dc.state in regions else "northeast"
    )

    schedule_form = ScheduleForm(
        first_run_stops=4, has_second_runs=1, second_run_stops=3
    )
    truck_choices = []
    for truck in trucks:
        truck_choices.append(truck)
    schedule_form.truck_id.choices = [
        (
            int(truck.id),
            f"Truck: {truck.number}, Driver: {truck.truck_driver.first_name} {truck.truck_driver.last_name}",
        )
        for truck in truck_choices
    ]

    if schedule_form.validate_on_submit():
        start_date = request.form.get("start_date")
        first_run_stops = request.form.get("first_run_stops")
        has_second_runs = request.form.get("has_second_runs")
        second_run_stops = request.form.get("second_run_stops")
        truck_id = request.form.get("truck_id")

        new_schedule = Schedule(
            start_date=start_date,
            first_run_stops=first_run_stops,
            has_second_runs=has_second_runs,
            second_run_stops=second_run_stops,
            truck_id=truck_id,
        )
        db.session.add(new_schedule)
        db.session.commit()
        return redirect("/dashboard")

    return render_template(
        "/schedule/dashboard.html",
        schedule_form=schedule_form,
        schedules=schedules,
        trucks=trucks,
    )
