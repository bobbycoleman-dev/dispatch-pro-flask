from flask import Blueprint, flash, render_template, redirect, request, session
from flask_app.models.distribution_center import DistributionCenter
from flask_app.models.dc_region import DCRegion
from flask_login import login_user, logout_user, current_user
from flask_app.forms.register import RegisterForm
from flask_app.forms.login import LoginForm
from flask_app.extensions import bcrypt, db, login_manager
from flask_app.models.user import User

bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    """User loader for Flask-Login."""

    return User.query.get(int(user_id))


@bp.route("/auth/register", methods=["GET", "POST"])
def register():
    """Displays the register page."""

    form = RegisterForm()
    form.dc_id.choices = [
        (int(dc.id), dc.nickname) for dc in DistributionCenter.query.all()
    ]

    if form.validate_on_submit():
        # Get valid user input
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")
        dc_id = request.form.get("dc_id")

        # Check if the user's email exists
        potential_user = User.query.filter_by(email=email).first()
        if potential_user:
            flash("Email in use.")
            return redirect("/users/user_settings")

        # Hash the password
        hashed = bcrypt.generate_password_hash(password)

        # Create user, add to db
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed,
            role=role,
            dc_id=dc_id,
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect("/users/user_settings")

    return redirect("/users/user_settings")


@bp.route("/auth/login", methods=["GET", "POST"])
def login():
    """Displays the login page."""

    form = LoginForm()

    if form.validate_on_submit():
        # Get the valid user input
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user's email exists
        potential_user = User.query.filter_by(email=email).first()
        if not potential_user:
            flash("Invalid credentials.")
            return redirect("/auth/login")

        user = potential_user

        # Check password validity
        if not bcrypt.check_password_hash(user.password, password):
            flash("Invalid credentials.")
            return redirect("/auth/login")

        # Log the user in
        login_user(user)

        return redirect("/dashboard")

    return render_template("/auth/login.html", form=form)


@bp.get("/auth/logout")
def logout():
    """Logs out the current user."""

    logout_user()
    return redirect("/")
