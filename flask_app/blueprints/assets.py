from flask_app.models.distribution_center import DistributionCenter
from flask_app.models.truck import Truck
from flask_app.models.driver import Driver
from flask_app.models.dc_region import DCRegion
from flask_app.forms.truck import TruckForm
from flask_app.forms.driver import DriverForm
from flask_login import current_user
from flask_app.extensions import db
from flask import Blueprint, redirect, render_template, request

bp = Blueprint("assets", __name__, url_prefix="/assets")


@bp.get("/asset_settings")
def asset_settings():
    dc_choices = []
    if current_user.role == 1:
        for dc in DistributionCenter.query.all():
            dc_choices.append(dc)
    elif current_user.role == 2:
        if current_user.user_dc.region == "South":
            for dc in DistributionCenter.query.filter(
                DistributionCenter.region == "South"
            ):
                dc_choices.append(dc)
        else:
            for dc in DistributionCenter.query.filter(
                DistributionCenter.region == "Northeast"
            ):
                dc_choices.append(dc)
    else:
        for dc in DistributionCenter.query.filter(
            DistributionCenter.id == current_user.user_dc.id
        ):
            dc_choices.append(dc)

    driver_choices = []
    if current_user.role == 1:
        for driver in Driver.query.all():
            driver_choices.append(driver)
    elif current_user.role == 2:
        if current_user.user_dc.region == "South":
            for driver in Driver.query.join(DistributionCenter.drivers).filter(
                DistributionCenter.region == "South"
            ):
                driver_choices.append(driver)
        else:
            for driver in Driver.query.join(DistributionCenter.drivers).filter(
                DistributionCenter.region == "Northeast"
            ):
                driver_choices.append(driver)
    else:
        for driver in Driver.query.filter(Driver.dc_id == current_user.user_dc.id):
            driver_choices.append(driver)

    truck_form = TruckForm()
    truck_form.dc_id.choices = [(int(dc.id), dc.nickname) for dc in dc_choices]
    truck_form.driver_id.choices = [
        (int(driver.id), driver.first_name) for driver in driver_choices
    ]
    driver_form = DriverForm()
    driver_form.dc_id.choices = [(int(dc.id), dc.nickname) for dc in dc_choices]

    if current_user.role == 1:
        trucks = Truck.query.all()
        drivers = Driver.query.all()
    elif current_user.role == 2:
        if current_user.user_dc.region == "South":
            trucks = Truck.query.join(DistributionCenter.trucks).filter(
                DistributionCenter.region == "South"
            )
            drivers = Driver.query.join(DistributionCenter.drivers).filter(
                DistributionCenter.region == "South"
            )
        else:
            trucks = Truck.query.join(DistributionCenter.trucks).filter(
                DistributionCenter.region == "Northeast"
            )
            drivers = Driver.query.join(DistributionCenter.drivers).filter(
                DistributionCenter.region == "Northeast"
            )
    else:
        trucks = Truck.query.filter(Truck.dc_id == current_user.user_dc.id)
        drivers = Driver.query.filter(Driver.dc_id == current_user.user_dc.id)

    return render_template(
        "/trucks_drivers/asset_settings.html",
        trucks=trucks,
        drivers=drivers,
        truck_form=truck_form,
        driver_form=driver_form,
    )


@bp.post("/create/truck")
def create_truck():
    dc_choices = []
    if current_user.role == 1:
        for dc in DistributionCenter.query.all():
            dc_choices.append(dc)
    elif current_user.role == 2:
        if current_user.user_dc.region == "South":
            for dc in DistributionCenter.query.filter(
                DistributionCenter.region == "South"
            ):
                dc_choices.append(dc)
        else:
            for dc in DistributionCenter.query.filter(
                DistributionCenter.region == "Northeast"
            ):
                dc_choices.append(dc)
    else:
        for dc in DistributionCenter.query.filter(
            DistributionCenter.id == current_user.user_dc.id
        ):
            dc_choices.append(dc)

    driver_choices = []
    if current_user.role == 1:
        for driver in Driver.query.all():
            driver_choices.append(driver)
    elif current_user.role == 2:
        if current_user.user_dc.region == "South":
            for driver in Driver.query.join(DistributionCenter.drivers).filter(
                DistributionCenter.region == "South"
            ):
                driver_choices.append(driver)
        else:
            for driver in Driver.query.join(DistributionCenter.drivers).filter(
                DistributionCenter.region == "Northeast"
            ):
                driver_choices.append(driver)
    else:
        for driver in Driver.query.filter(Driver.dc_id == current_user.user_dc.id):
            driver_choices.append(driver)

    truck_form = TruckForm()
    truck_form.dc_id.choices = [(int(dc.id), dc.nickname) for dc in dc_choices]
    truck_form.driver_id.choices = [
        (int(driver.id), driver.first_name) for driver in driver_choices
    ]

    if truck_form.validate_on_submit():
        number = request.form.get("number")
        make = request.form.get("make")
        model = request.form.get("model")
        year = request.form.get("year")
        vin = request.form.get("vin")
        dc_id = request.form.get("dc_id")
        driver_id = request.form.get("driver_id")

        new_truck = Truck(
            number=number,
            make=make,
            model=model,
            year=year,
            vin=vin,
            dc_id=dc_id,
            driver_id=driver_id,
        )
        db.session.add(new_truck)
        db.session.commit()
        return redirect("/assets/asset_settings")

    return redirect("/assets/asset_settings")


@bp.post("/create/driver")
def create_driver():
    dc_choices = []
    if current_user.role == 1:
        for dc in DistributionCenter.query.all():
            dc_choices.append(dc)
    elif current_user.role == 2:
        if current_user.user_dc.region == "South":
            for dc in DistributionCenter.query.filter(
                DistributionCenter.region == "South"
            ):
                dc_choices.append(dc)
        else:
            for dc in DistributionCenter.query.filter(
                DistributionCenter.region == "Northeast"
            ):
                dc_choices.append(dc)
    else:
        for dc in DistributionCenter.query.filter(
            DistributionCenter.id == current_user.user_dc.id
        ):
            dc_choices.append(dc)

    driver_form = DriverForm()
    driver_form.dc_id.choices = [(int(dc.id), dc.nickname) for dc in dc_choices]

    if driver_form.validate_on_submit():
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        license_type = request.form.get("license_type")
        license_exp = request.form.get("license_exp")
        dot_exp = request.form.get("dot_exp")
        dc_id = request.form.get("dc_id")

        new_driver = Driver(
            first_name=first_name,
            last_name=last_name,
            license_type=license_type,
            license_exp=license_exp,
            dot_exp=dot_exp,
            dc_id=dc_id,
        )
        db.session.add(new_driver)
        db.session.commit()
        return redirect("/assets/asset_settings")

    return redirect("/assets/asset_settings")
