from flask_wtf import FlaskForm
from wtforms import DateField, StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length


class DriverForm(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired(), Length(2, 45)])
    last_name = StringField("Last Name:", validators=[Length(2, 45)])
    license_type = SelectField(
        "License Type:",
        choices=[
            ("non_cdl", "Non-CDL (Class C)"),
            ("cdlb", "CDL-B"),
            ("cdla", "CDL-A"),
        ],
    )
    license_exp = DateField("License Expiration:")
    dot_exp = DateField("DOT Expiration:")
    dc_id = SelectField("Location:")
