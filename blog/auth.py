"""
Authentication Module
---------------------

This module defines all the routes and logic related to
user authentication.

It includes login, logout, and user registration.

Routes:
    - /register
    - /login
    - /logout
    - /edit_profile

Uses the 'login_required' decorator to protect
routes that require authentication.

"""


from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    g,
)
from .models.auth_register import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models.posts import Posts
from werkzeug.utils import secure_filename
import functools


bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


# register form
@bp_auth.route("/register", methods=["GET", "POST"])
def register():
    """Handles the registration of new users.

    This endpoint accepts GET methods to display the registration form and POST
    methods to process the form data.

    Args:
        None, but expects to receive 'name', 'email', and 'password'
        from the form.

    Returns:
        render_template: Returns the registration form template or redirects
        to the login page upon successful registration.

    Raises:
        None: Doesn't raise explicit exceptions, but may flash error messages.
    """

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(name, email, generate_password_hash(password))

        error = None
        user_name_validator = User.query.filter_by(name=name).first()
        email_validator = User.query.filter_by(email=email).first()

        if not user_name_validator and not email_validator:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))

        else:
            if user_name_validator is not None:
                error = "El nombre de suario ya existe, elija otro!"
                flash(error)

            elif email_validator is not None:
                error = "El Email ya existe, elija otro!"
                flash(error)

    return render_template("authentication/register.html")


# login form


@bp_auth.route("/login", methods=["GET", "POST"])
def login():
    """Handles the login of previously registered users.

    This endpoint accepts GET methods to display the login
    form and POST methods to process the form data.

    Args:
        None, but expects to receive email and password from the form
        via POST.

    Returns:
        Render_template: Returns the login form template or redirects
        to the index template in case of a successful login.

    Raises:
        None: Does not raise explicit exceptions, but may flash
        error messages upon login failure.
    """

    error = None

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None:
            error = "usuario no encontrado"
        elif not check_password_hash(user.password, password):
            error = "contraseña incorrecta"

        if error is None:
            session.clear()
            session["user.id"] = user.id

            return redirect(url_for("main.index"))

    return render_template("authentication/login.html", error=error)


# keep user logged


@bp_auth.before_app_request
def load_user():
    user_id = session.get("user.id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


# protecting the views


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view


# show profile


@bp_auth.route("/profile", methods=["GET"])
@login_required
def profile():
    user = User.query.get_or_404(g.user.id)
    photo = get_picture(id)
    posts = Posts.query.filter_by(author=g.user.id).all()
    post_count = Posts.query.filter_by(author=g.user.id).count()

    return render_template(
        "authentication/profile.html",
        user=user,
        photo=photo,
        posts=posts,
        post_count=post_count,
    )


# edit profile
@bp_auth.route("/edit_profile/<int:id>", methods=["GET", "POST"])
@login_required
def edit_profile(id):
    """Allow to edit profile from registered users.

    This endpoint accepts GET methods to display the edit view
    form and POST methods to save the new data.

    Args:
        id (int): User id.

    Returns:
        Render_template: Returns the edit form template or redirects
        to login in case user is not loged.

    Raises:
        None: Does not raise explicit exceptions, but may flash
        error messages upon login failure.
    """
    user = User.query.get_or_404(id)
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        error = None

        if password and len(password) < 6:
            error = "La contraseña debe tener más de 6 caracteres."

        if error is not None:
            flash(error)
        else:
            if password:
                user.password = generate_password_hash(password)

            if request.files["image"]:
                photo = request.files["image"]
                photo.save(
                    f"blog/static/media/{secure_filename(photo.filename)}"
                )
                user.photo = f"media/{secure_filename(photo.filename)}"

            if name and name != "":
                user.name = name

            if email and email != "":
                user.email = email

            db.session.commit()
            return redirect(url_for("auth.profile"))

    return render_template("authentication/edit_profile.html")


# load image


def get_picture(id):
    user = User.query.get_or_404(g.user.id)
    return user.photo if user.photo is not None else None


# close session


@bp_auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.index"))
