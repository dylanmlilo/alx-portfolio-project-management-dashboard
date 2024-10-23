from flask import Blueprint, request, redirect, url_for, flash, jsonify
from models.engine.database import session
from models.gis import ResponsiblePerson
from flask_login import login_required
from models.decorators import required_roles


gis_resp_person_bp = Blueprint('gis_resp_person', __name__)


@gis_resp_person_bp.route("/insert_gis_resp_person_data", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def insert_gis_resp_person_data():
    """
    Inserts the GIS responsible person data into the database and
    redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            name = request.form.get('responsible_person_name')
            designation = request.form.get('designation')

            new_responsible_person = ResponsiblePerson(name=name, designation=designation)
            session.add(new_responsible_person)
            session.commit()
            flash('Data inserted successfully!', 'success')
            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            flash(f'An error occurred while inserting data: {str(e)}', 'error')
            return redirect(url_for('gis_data.gis_data'))

        finally:
            session.close()


@gis_resp_person_bp.route("/update_gis_resp_person_data/<int:gis_resp_person_data_id>", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def update_gis_resp_person_data(gis_resp_person_data_id):
    """
    Updates the GIS responsible person data in the database and
    redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            responsible_person = session.query(ResponsiblePerson).filter_by(id=gis_resp_person_data_id).first()
            if responsible_person:
                responsible_person.name = request.form.get('responsible_person_name')
                responsible_person.designation = request.form.get('designation')

                session.commit()
                flash('Data updated successfully!', 'success')
            else:
                flash('Responsible person not found.', 'error')

            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            flash(f'An error occurred while updating data: {str(e)}', 'error')
            return redirect(url_for('gis_data.gis_data'))

        finally:
            session.close()


@gis_resp_person_bp.route("/delete_gis_resp_person_data/<int:gis_resp_person_data_id>")
@login_required
@required_roles("admin", "admin_gis")
def delete_gis_resp_person_data(gis_resp_person_data_id):
    """
    Deletes the GIS responsible person data from the database and
    redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    try:
        responsible_person = session.query(ResponsiblePerson).filter_by(id=gis_resp_person_data_id).first()
        if responsible_person:
            session.delete(responsible_person)
            session.commit()
            flash('Data deleted successfully!', 'success')
        else:
            flash('Responsible person not found.', 'error')

        return redirect(url_for('gis_data.gis_data'))

    except Exception as e:
        session.rollback()
        flash('An error occurred while deleting the responsible person. It seems that the responsible person is associated with an activity that cannot be empty. Please check the activities associated with the responsible person.', 'error')
        return redirect(url_for('gis_data.gis_data'))

    finally:
        session.close()
