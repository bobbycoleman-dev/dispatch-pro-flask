from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired(), Length(2, 45)])
    last_name = StringField("Last Name:", validators=[DataRequired(), Length(2, 45)])
    email = EmailField("Email:", validators=[DataRequired(), Email()])
    dc_id = SelectField("Location:")
    role = SelectField(
        "Role:",
        choices=[
            (9, "--Please select a Role--"),
            (1, "Admin"),
            (2, "Regional"),
            (3, "Dispatcher"),
            (4, "Operations"),
            (5, "Viewer"),
        ],
    )
    password = PasswordField("Password:", validators=[Length(8, 45)])
    confirm_password = PasswordField(
        "Confirm Password:", validators=[EqualTo("password", "passwords must match")]
    )
