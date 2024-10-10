from flask import Blueprint, render_template
from models.strategic import StrategicTask


strategic_bp = Blueprint('strategic', __name__)


@strategic_bp.route("/StrategicPlanning", strict_slashes=False)
def strategic_planning():
    strategic_data = StrategicTask.strategic_tasks_to_dict_list
    return render_template("strategic_planning.html", strategic_data=strategic_data)