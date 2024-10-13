from flask import Blueprint, render_template
from models.projects import projects_data_to_dict_list
from models.plot_functions import today_date, plot_servicing_page_charts


sections_bp = Blueprint('sections', __name__)


@sections_bp.route("/Servicing", strict_slashes=False)
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
    projects_data = projects_data_to_dict_list(1)
    servicing_data_JSON = plot_servicing_page_charts()
    formatted_date = today_date()
    return render_template("servicing.html", projects_data=projects_data,
                           today_date=formatted_date,
                           servicing_data_JSON=servicing_data_JSON)