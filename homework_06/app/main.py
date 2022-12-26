from os import getenv

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import redirect

from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.exc import DatabaseError

from models import db

from werkzeug.exceptions import NotFound

from views.users import users_app

app = Flask(
    __name__,
)
app.register_blueprint(users_app, url_prefix="/users")

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

csft = CSRFProtect(app)

db.app = app
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")


@app.errorhandler(DatabaseError)
def handle_database_error(error):
    return render_template("dberror.html"), 404
