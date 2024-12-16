from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, logout_user, current_user, login_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)

# Homepage Route
@views.route('/')
def home():
    return render_template('home.html')  # Welcome homepage

# Profile Route (Only accessible after login)
@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html')  # Page with profile update message

# Logout Route
@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))  # Redirect to homepage after logout
