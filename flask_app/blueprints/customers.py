from flask_app.forms.customer import CustomerForm
from flask_app.forms.address import AddressForm
from flask_app.models.customer import Customer
from flask_app.models.address import Address
from flask_login import current_user
from flask_app.extensions import db
from flask import Blueprint, redirect, render_template, request

bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.route("/customer_settings", methods=["GET", "POST"])
def customer_settings():
    customers = Customer.query.filter(Customer.dc_id == current_user.user_dc.id)
    addresses = Address.query.all()

    customer_form = CustomerForm(dc_id=current_user.user_dc.id)

    if customer_form.validate_on_submit():
        company_name = request.form.get("company_name")
        poc_first_name = request.form.get("poc_first_name")
        poc_last_name = request.form.get("poc_last_name")
        poc_number = request.form.get("poc_number")
        dc_id = request.form.get("dc_id")

        new_customer = Customer(
            company_name=company_name,
            poc_first_name=poc_first_name,
            poc_last_name=poc_last_name,
            poc_number=poc_number,
            dc_id=dc_id,
        )
        db.session.add(new_customer)
        db.session.commit()
        return redirect("/customers/customer_settings")

    address_form = AddressForm()
    customer_choices = []
    for customer in customers:
        customer_choices.append(customer)
    address_form.customer_id.choices = [
        (int(customer.id), customer.company_name) for customer in customer_choices
    ]

    if address_form.validate_on_submit():
        street = request.form.get("street")
        city = request.form.get("city")
        state = request.form.get("state")
        zip_code = request.form.get("zip_code")
        customer_id = request.form.get("customer_id")

        new_address = Address(
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            customer_id=customer_id,
        )
        db.session.add(new_address)
        db.session.commit()
        return redirect("/customers/customer_settings")

    return render_template(
        "/customers/customer_settings.html",
        customer_form=customer_form,
        address_form=address_form,
        customers=customers,
        addresses=addresses,
    )
