from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length


class TruckForm(FlaskForm):
    number = StringField("Truck Number:", validators=[DataRequired(), Length(1, 45)])
    make = StringField("Make:", validators=[Length(2, 45)])
    model = StringField("Model:", validators=[Length(2, 45)])
    year = IntegerField("Year:")
    vin = StringField("Vin:", validators=[Length(17, 17)])
    dc_id = SelectField("Location:")
    driver_id = SelectField("Driver:")
