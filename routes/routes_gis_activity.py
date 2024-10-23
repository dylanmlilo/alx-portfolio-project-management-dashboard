from flask import Blueprint, request, redirect, url_for, flash, jsonify
from models.engine.database import session
from models.gis import Activity
from flask_login import login_required
from models.decorators import required_roles


gis_activity_bp = Blueprint('gis_activity', __name__)


@gis_activity_bp.route("/insert_gis_activity_data", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def insert_gis_activity_data():
    """
    Inserts the GIS data into the database and redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            activity = request.form.get('activity_name')
            output_id = request.form.get('output_id')
            responsible_person_id = request.form.get('responsible_person_id')

            new_activity = Activity(
                activity=activity,
                output_id=output_id,
                responsible_person_id=responsible_person_id
            )
            session.add(new_activity)
            session.commit()
            flash('Data inserted successfully!', 'success')
            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            flash('An error occurred while inserting the data. It looks like the output or responsible person you selected is not valid. Please make sure that the output or responsible person exists before adding the activity.', 'error')
            
            return redirect(url_for('gis_data.gis_data'))
        

        finally:
            session.close()


@gis_activity_bp.route("/update_gis_activity_data/<int:gis_activity_data_id>", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def update_gis_activity_data(gis_activity_data_id):
    """
    Updates the GIS data in the database and redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            activity = session.query(Activity).filter_by(id=gis_activity_data_id).first()
            if activity:
                activity.activity = request.form.get('activity_name')
                activity.output_id = request.form.get('output_id')
                activity.responsible_person_id = request.form.get('responsible_person_id')

                session.commit()
                flash('Data updated successfully!', 'success')
            else:
                flash('Activity not found.', 'error')

            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            flash('An error occurred while updating the data. It looks like the output or responsible person you selected is not valid. Please make sure that the output or responsible person exists before updating the activity.', 'error')
            return redirect(url_for('gis_data.gis_data'))

        finally:
            session.close()


@gis_activity_bp.route("/delete_gis_activity_data/<int:gis_activity_data_id>")
@login_required
@required_roles("admin", "admin_gis")
def delete_gis_activity_data(gis_activity_data_id):
    """
    Deletes the GIS data from the database and redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    try:
        activity = session.query(Activity).filter_by(id=gis_activity_data_id).first()
        if activity:
            session.delete(activity)
            session.commit()
            flash('Data deleted successfully!', 'success')
        else:
            flash('Activity not found.', 'error')

        return redirect(url_for('gis_data.gis_data'))

    except Exception as e:
        session.rollback()
        flash('An error occurred while deleting the activity. It seems that the activity is associated with an task that cannot be empty. Please check the tasks associated with the Activity.', 'error')

        return redirect(url_for('gis_data.gis_data'))

    finally:
        session.close()

