from flask import Blueprint, request, redirect, url_for, flash, jsonify
from models.engine.database import session
from models.gis import Output
from flask_login import login_required
from models.decorators import required_roles


gis_output_bp = Blueprint('gis_output', __name__)


@gis_output_bp.route("/insert_gis_output_data", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def insert_gis_output_data():
    """
    Inserts the GIS data into the database and redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or a
        JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            name = request.form.get('output_name')

            new_output = Output(name=name)
            session.add(new_output)
            session.commit()
            flash('Data inserted successfully!', 'success')
            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            flash(f'An error occurred while inserting data: {str(e)}', 'error')
            return redirect(url_for('gis_data.gis_data'))

        finally:
            session.close()


@gis_output_bp.route("/update_gis_output_data/<int:gis_output_data_id>", methods=['POST'])
@login_required
@required_roles("admin", "admin_gis")
def update_gis_output_data(gis_output_data_id):
    """
    Updates the GIS data in the database and redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or
        a JSON response with an error message.
    """
    if request.method == 'POST':
        try:
            output = session.query(Output).filter_by(id=gis_output_data_id).first()
            if output:
                output.name = request.form.get('output_name')
                session.commit()
                flash('Data updated successfully!', 'success')
            else:
                flash('Output not found.', 'error')
            return redirect(url_for('gis_data.gis_data'))

        except Exception as e:
            session.rollback()
            flash(f'An error occurred while updating data: {str(e)}', 'error')
            return redirect(url_for('gis_data.gis_data'))

        finally:
            session.close()


@gis_output_bp.route("/delete_gis_output_data/<int:gis_output_data_id>")
@login_required
@required_roles("admin", "admin_gis")
def delete_gis_output_data(gis_output_data_id):
    """
    Deletes the GIS data from the database and redirects to the GIS data page.

    Returns:
        flask.Response: A redirect response to the GIS data page or a
        JSON response with an error message.
    """
    try:
        output = session.query(Output).filter_by(id=gis_output_data_id).first()
        if output:
            session.delete(output)
            session.commit()
            flash('Data deleted successfully!', 'success')
        else:
            flash('Output not found.', 'error')
        return redirect(url_for('gis_data.gis_data'))

    except Exception as e:
        session.rollback()
        flash('An error occurred while deleting the output. It seems that the output is associated with an activity that cannot be empty. Please check the activities associated with the output.', 'error')
        return redirect(url_for('gis_data.gis_data'))

    finally:
        session.close()
