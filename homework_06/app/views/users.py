from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
)
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from models import db, User
from views.forms.users import UserForm

users_app = Blueprint(
    "users_app",
    __name__,
)


@users_app.route("/", endpoint="list")
def users_list():
    users = User.query.all()
    return render_template(
        "users/list.html",
        users=users,
    )


@users_app.route(
    "/<int:user_id>/",
    methods=["GET"],
    endpoint="details",
)
def get_user_by_id(user_id: int):
    user = User.query.get_or_404(
        user_id,
        description=f"User #{user_id} not found!",
    )

    return render_template(
        "users/details.html",
        user=user,
    )


@users_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_user():
    form = UserForm()

    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400

    user_name = form.name.data
    user_username = form.username.data
    user_email = form.email.data
    user = User(name=user_name, username=user_username, email=user_email)
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create user {user_username!r}")

    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
