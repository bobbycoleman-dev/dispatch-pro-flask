from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length


class AddressForm(FlaskForm):
    street = StringField("Street:", validators=[DataRequired(), Length(2, 45)])
    city = StringField("City:", validators=[DataRequired(), Length(2, 45)])
    state = StringField("State:", validators=[DataRequired(), Length(2, 2)])
    zip_code = IntegerField("Zip Code:", validators=[DataRequired()])
    customer_id = SelectField("Customer:")
