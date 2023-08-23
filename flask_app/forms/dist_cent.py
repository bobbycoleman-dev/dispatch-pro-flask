from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class DistributionCenterForm(FlaskForm):
    nickname = StringField("Location Name:", validators=[DataRequired(), Length(2, 45)])
    street = StringField("Street:", validators=[DataRequired(), Length(2, 45)])
    city = StringField("City:", validators=[DataRequired(), Length(2, 45)])
    state = StringField("State:", validators=[DataRequired(), Length(2, 2)])
    zip_code = IntegerField("Zip Code:", validators=[DataRequired()])
