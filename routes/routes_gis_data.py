from flask import Blueprint, render_template
from models.gis import gis_data_to_dict_list


gis_data_bp = Blueprint('gis_data', __name__)


@gis_data_bp.route("/GIS", strict_slashes=False)
def gis():
    gis_data_list = gis_data_to_dict_list()
    return render_template("gis.html", gis_data_list=gis_data_list)