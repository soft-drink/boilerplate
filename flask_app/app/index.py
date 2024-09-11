from . import APP_NAME

from flask import Blueprint, render_template


bp = Blueprint("front_page", __name__)


@bp.route("/")
def index():
    return render_template("index.html", title=APP_NAME)

