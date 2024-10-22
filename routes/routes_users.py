from flask import (
    Blueprint, render_template, request,
    redirect, url_for, jsonify, flash
    )
from flask_login import login_required
from models.users import Users
from models.plot_functions import today_date
from models.engine.database import session
from models.decorators import required_roles


users_bp = Blueprint('users', __name__)


@users_bp.route("/users_data", strict_slashes = False)
@login_required
@required_roles('admin')
def users():
    """
    Displays a list of all users in the database.

    This view function renders the users_data.html template with the list of all
    users in the database. The list is ordered by the user's name.

    Args:
        None

    Returns:
        flask.Response: A rendered template with the list of all users in the
        database.
    """

    todays_date = today_date()
    users_data = Users.user_data_to_dict_list()
    return render_template("users_data.html", users_data=users_data,
                           today_date=todays_date)


@users_bp.route("/insert_user_data", strict_slashes=False, methods=["POST", "GET"])
@login_required
@required_roles('admin')
def insert_user_data():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            surname = request.form.get('surname')
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')
            role = request.form.get('role')

            existing_username = session.query(Users).filter_by(username=username).first()
            if existing_username:
                flash('Username already exists', 'error')
                return redirect(url_for('users.users'))

            existing_email = session.query(Users).filter_by(email=email).first()
            if existing_email:
                flash('Email already exists', 'error')
                return redirect(url_for('users.users'))

            new_user = Users(name, surname, username, password, email, role)
            session.add(new_user)
            session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('users.users'))

        except Exception as e:
            session.rollback()
            flash('An error occurred: {}'.format(str(e)), 'error')
            return redirect(url_for('users.users'))
        finally:
            session.close()



@users_bp.route("/update_user_data/<int:user_data_id>", strict_slashes=False, methods=["POST"])
@login_required
@required_roles('admin')
def update_user_data(user_data_id):
    """
    Update user data.

    Args:
        user_data_id (int): The id of the user to update.

    Returns:
        A redirect to the users page if the update is successful, a 400 error with
        an error message if the update fails, or a 404 error if the user is not found.
    """
    if request.method == "POST":
        user = session.query(Users).filter_by(id=user_data_id).first()
        if user:
            try:
                name = request.form.get('name')
                surname = request.form.get('surname')
                new_username = request.form.get('username')
                password = request.form.get('password')
                email = request.form.get('email')
                role = request.form.get('role')

                existing_username = session.query(Users).filter_by(username=new_username).filter(Users.id != user_data_id).first()
                if existing_username:
                    flash('Username already exists', 'error')
                    return redirect(url_for('users.users'))

                existing_email = session.query(Users).filter_by(email=email).filter(Users.id != user_data_id).first()
                if existing_email:
                    flash('Email already exists', 'error')
                    return redirect(url_for('users.users'))

                user.name = name
                user.surname = surname
                user.username = new_username
                user.password = password
                user.email = email
                user.role = role

                session.commit()
                flash('User data updated successfully!', 'success')
                return redirect(url_for('users.users'))

            except Exception as e:
                session.rollback()
                flash(f'An error occurred: {str(e)}', 'error')
                return redirect(url_for('users.edit_user', user_data_id=user_data_id))

            finally:
                session.close()
        else:
            flash('User not found.', 'error')
            return redirect(url_for('users.users'))

        

@users_bp.route("/delete_user_data/<int:user_data_id>")
@login_required
@required_roles('admin')
def delete_user_data(user_data_id):
    """
    Deletes a user from the database.

    Args:
        user_data_id (int): The ID of the user to delete.

    Returns:
        A redirect to the users page if the user is successfully deleted,
        or a 404 error with an error message if the user is not found.
    """
    user = session.query(Users).filter_by(id=user_data_id).first()
    if user:
        try:
            session.delete(user)
            session.commit()
            flash('User deleted successfully!', 'success')
            return redirect(url_for('users.users'))
        except Exception as e:
            session.rollback()
            flash(f'An error occurred while deleting the user: {str(e)}', 'error')
            return redirect(url_for('users.users'))
        finally:
            session.close()
    else:
        flash('User not found....', 'error')
        return redirect(url_for('users.users'))