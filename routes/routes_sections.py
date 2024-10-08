from flask import Blueprint, render_template


sections_bp = Blueprint('sections', __name__)


@sections_bp.route("/Servicing", strict_slashes=False)
def servicing():
    return render_template("servicing.html")