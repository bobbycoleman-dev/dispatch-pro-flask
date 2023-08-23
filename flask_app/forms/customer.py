from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
import phonenumbers


class CustomerForm(FlaskForm):
    company_name = StringField(
        "Company Name:", validators=[DataRequired(), Length(2, 45)]
    )
    poc_first_name = StringField(
        "POC First Name:", validators=[DataRequired(), Length(2, 45)]
    )
    poc_last_name = StringField(
        "POC Last Name:", validators=[DataRequired(), Length(2, 45)]
    )
    poc_number = StringField("POC Phone Number:", validators=[DataRequired()])
    dc_id = HiddenField()

    def validate_phone(self, poc_number):
        try:
            p = phonenumbers.parse(poc_number.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError("Invalid phone number")
