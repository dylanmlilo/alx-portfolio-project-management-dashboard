from flask import Blueprint, render_template
from flask_login import login_required
from models.projects import ProjectsData
from models.plot_functions import today_date, plot_servicing_page_charts


sections_bp = Blueprint('sections', __name__)


@sections_bp.route("/Servicing", strict_slashes=False)
@login_required
def servicing():
    """
    Renders the 'servicing.html' template with project
    data for servicing contracts.

    This function fetches project data for servicing contracts,
    generates a bar chart,
    and renders the 'servicing.html' template with the necessary data.

    Returns:
        Flask.Response: The rendered template.
    """
    projects_data = ProjectsData.projects_data_to_dict_list(1)
    servicing_data_JSON = plot_servicing_page_charts()
    formatted_date = today_date()
    return render_template("servicing.html", projects_data=projects_data,
                           today_date=formatted_date,
                           servicing_data_JSON=servicing_data_JSON)