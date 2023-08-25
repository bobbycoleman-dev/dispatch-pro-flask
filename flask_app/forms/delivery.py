from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, HiddenField, IntegerField
from wtforms.validators import DataRequired


class DeliveryForm(FlaskForm):
    date = HiddenField()
    dc_id = HiddenField()
    truck = SelectField("Truck:")
    is_first_run = SelectField(
        "First or Second Run:",
        validators=[DataRequired()],
        choices=[(1, "First Run"), (2, "Second Run")],
        coerce=int,
    )
    day = SelectField(
        "Delivery Day:",
        validators=[DataRequired()],
        choices=[
            (1, "Monday"),
            (2, "Tuesday"),
            (3, "Wednesday"),
            (4, "Thursday"),
            (5, "Friday"),
            (6, "Saturday"),
        ],
        coerce=int,
    )
    stop_num = SelectField(
        "Stop Number:",
        validators=[DataRequired()],
        choices=[
            (1, "Stop 1"),
            (2, "Stop 2"),
            (3, "Stop 3"),
            (4, "Stop 4"),
        ],
        coerce=int,
    )
    customer_id = SelectField("Customer:")
    address_id = SelectField("Address:")
