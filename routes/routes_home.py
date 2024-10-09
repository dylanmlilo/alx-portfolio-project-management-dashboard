from flask import Blueprint, render_template
from models.projects import projects_data_to_dict_list


home_bp = Blueprint('home', __name__)


@home_bp.route("/home", strict_slashes=False)
def index():
    return render_template("home.html")