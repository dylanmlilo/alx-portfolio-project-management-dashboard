from flask import Blueprint, render_template
from models.projects import projects_data_to_dict_list


sections_bp = Blueprint('sections', __name__)


@sections_bp.route("/Servicing", strict_slashes=False)
def servicing():
    projects_data =  projects_data_to_dict_list()
    return render_template("servicing.html",  projects_data=projects_data)
