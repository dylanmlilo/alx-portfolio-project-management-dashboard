from flask import Blueprint, render_template
from flask_login import login_required
from models.plot_functions import today_date
from models.gis import gis_data_to_dict_list
from models.plot_functions import today_date
from itertools import groupby


gis_data_bp = Blueprint('gis_data', __name__)


@gis_data_bp.route("/GIS", strict_slashes=False)
@login_required
def gis():
    """
    Function to handle GIS route.

    Retrieves GIS data, responsible persons, progress data,
    and today's date, then renders the gis.html template.

    Parameters:
    - None

    Returns:
    - Rendered template "gis.html" with today's date, GIS data,
    progress data, and responsible persons.

    """
    formatted_date = today_date()
    gis_data = gis_data_to_dict_list()


    gis_data_grouped = []
    for key, group in groupby(gis_data, key=lambda x: x["output_name"]):
        gis_data_grouped.append((key, list(group)))
    return render_template("gis.html", today_date=formatted_date,
                           gis_data_grouped=gis_data_grouped)