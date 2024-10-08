from flask import Blueprint, render_template


gis_data_bp = Blueprint('gis_data', __name__)


@gis_data_bp.route("/GIS", strict_slashes=False)
def gis():
    return render_template("gis.html")