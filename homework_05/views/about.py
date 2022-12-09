from flask import Blueprint, render_template

about_app = Blueprint(
    "about_app",
    __name__,
)


@about_app.get("/", endpoint="about")
def about_main():
    return render_template("about.html")
