from flask import Blueprint, render_template
from models.plot_functions import today_date
from models.strategic import StrategicTask


strategic_bp = Blueprint('strategic', __name__)


@strategic_bp.route("/StrategicPlanning", strict_slashes=False)
def strategic_planning():
    """
    Function to handle Strategic Planning route.

    Retrieves strategic data list and today's date,
    then renders the strategic_planning.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "strategic_planning.html"
    with today's date and strategic data list.

    """
    strategic_data_list = StrategicTask.strategic_tasks_to_dict_list()
    formatted_date = today_date()
    return render_template("strategic_planning.html",
                           today_date=formatted_date,
                           strategic_data_list=strategic_data_list)