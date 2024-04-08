from flask import Blueprint, render_template, redirect, url_for
from auth import login_required

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html')

@main_bp.route('/portfolio')
@login_required
def portfolio():
    return render_template('main/index.html')