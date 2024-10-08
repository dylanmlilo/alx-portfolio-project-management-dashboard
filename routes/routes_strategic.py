from flask import Blueprint, render_template


strategic_bp = Blueprint('strategic', __name__)


@strategic_bp.route("/StrategicPlanning", strict_slashes=False)
def strategic_planning():
    return render_template("strategic_planning.html")