from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField, DateField
from wtforms.validators import DataRequired, Length


class ScheduleForm(FlaskForm):
    start_date = DateField("Start Date:", validators=[DataRequired()])
    first_run_stops = IntegerField("First Run Stop Count:", validators=[DataRequired()])
    has_second_runs = RadioField(
        "Include Second Runs?",
        validators=[DataRequired()],
        choices=[(1, "Yes"), (2, "No")],
    )
    second_run_stops = IntegerField(
        "Second Run Stop Count:", validators=[DataRequired()]
    )
    truck_id = SelectField("Assigned Truck:")
