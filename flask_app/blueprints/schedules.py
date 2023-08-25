from pprint import pprint
from datetime import date
from flask import Blueprint, render_template, redirect, request, jsonify
from flask_app.forms.schedule import ScheduleForm
from flask_app.forms.delivery import DeliveryForm
from flask_app.models.schedule import Schedule
from flask_app.models.delivery import Delivery
from flask_app.models.customer import Customer
from flask_app.models.address import Address
from flask_app.models.truck import Truck
from flask_login import current_user
from flask_app.extensions import db
from flask_app.models.dc_region import DCRegion

bp = Blueprint("schedules", __name__)
today = date.today()


@bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    trucks = Truck.query.filter(Truck.dc_id == current_user.dc_id)
    schedules = Schedule.query.join(Schedule.truck).filter(
        Truck.dc_id == current_user.dc_id
    )
    customers = Customer.query.filter(Customer.dc_id == current_user.dc_id)
    addresses = Address.query.all()
    deliveries = Delivery.query.all()
    regions = DCRegion().south
    current_user.region = (
        "south" if current_user.user_dc.state in regions else "northeast"
    )

    schedule_form = ScheduleForm(
        first_run_stops=4,
        has_second_runs=1,
        second_run_stops=3,
        dc_id=current_user.dc_id,
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
        dc_id = request.form.get("dc_id")
        start_date = request.form.get("start_date")
        first_run_stops = request.form.get("first_run_stops")
        has_second_runs = request.form.get("has_second_runs")
        second_run_stops = request.form.get("second_run_stops")
        truck_id = request.form.get("truck_id")

        new_schedule = Schedule(
            dc_id=dc_id,
            start_date=start_date,
            first_run_stops=first_run_stops,
            has_second_runs=has_second_runs,
            second_run_stops=second_run_stops,
            truck_id=truck_id,
        )
        db.session.add(new_schedule)
        db.session.commit()
        return redirect("/dashboard")

    delivery_form = DeliveryForm(date=today, dc_id=current_user.dc_id)
    customer_choices = []
    for customer in customers:
        customer_choices.append(customer)
    delivery_form.customer_id.choices = [
        (int(customer.id), customer.company_name) for customer in customer_choices
    ]

    delivery_form.truck.choices = [
        (int(schedule.id), schedule.truck.number) for schedule in schedules
    ]

    delivery_form.address_id.choices = [
        (
            int(address.id),
            f"{address.street}, {address.city}, {address.state} {address.zip_code}",
        )
        for address in addresses
    ]

    if delivery_form.validate_on_submit():
        dc_id = request.form.get("dc_id")
        date = request.form.get("date")
        is_first_run = request.form.get("is_first_run")
        stop_num = request.form.get("stop_num")
        customer_id = request.form.get("customer_id")
        address_id = request.form.get("address_id")
        schedule_id = request.form.get("schedule_id")

        new_delivery = Delivery(
            dc_id=dc_id,
            date=date,
            is_first_run=is_first_run,
            stop_num=stop_num,
            customer_id=customer_id,
            address_id=address_id,
            schedule_id=schedule_id,
        )
        db.session.add(new_delivery)
        db.session.commit()
        return redirect("/dashboard")

    return render_template(
        "/schedule/dashboard.html",
        schedule_form=schedule_form,
        delivery_form=delivery_form,
        schedules=schedules,
        trucks=trucks,
        deliveries=deliveries,
        addresses=addresses,
    )


@bp.post("/create/delivery")
def create_delivery():
    dc_id = request.form.get("dc_id")
    date = request.form.get("date")
    truck = request.form.get("truck")
    is_first_run = request.form.get("is_first_run")
    day = request.form.get("day")
    stop_num = request.form.get("stop_num")
    customer_id = request.form.get("customer_id")
    address_id = request.form.get("address_id")

    new_delivery = Delivery(
        dc_id=dc_id,
        date=date,
        is_first_run=is_first_run,
        stop_num=day + stop_num,
        customer_id=customer_id,
        address_id=address_id,
        schedule_id=truck,
    )
    db.session.add(new_delivery)
    db.session.commit()
    return jsonify(new_delivery.to_dict())


@bp.get("/deliveries")
def get_deliveries():
    deliveries = Delivery.query.filter(Delivery.dc_id == current_user.dc_id)
    results = []
    for delivery in deliveries:
        results.append(delivery.to_dict())
    pprint(deliveries)
    return jsonify(results)
