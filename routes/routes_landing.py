from flask import Blueprint, render_template, redirect, url_for, flash


landing_bp = Blueprint('landing', __name__)


def myForm():
    pass

@landing_bp.route('/', strict_slashes=False, methods=['GET', 'POST'])
def landing():
    form = myForm()
    return render_template('landing.html', form=form)