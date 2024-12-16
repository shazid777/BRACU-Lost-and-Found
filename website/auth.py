from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', category='success')
            return redirect(url_for('auth.profile'))  # Redirect to profile after login
        else:
            flash('Incorrect email or password.', category='danger')

    return render_template('login.html')

# Logout Route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.login'))

# Signup Route
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please log in or use another email.', category='danger')
        elif len(first_name) < 2:
            flash('First name must be at least 2 characters.', category='danger')
        elif password1 != password2:
            flash('Passwords do not match.', category='danger')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.', category='danger')
        else:
            # Add new user
            new_user = User(
                email=email, 
                first_name=first_name, 
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Now log in to your account.', category='success')
            return redirect(url_for('auth.login'))  # Redirect to login page

    return render_template('sign_up.html')

# Profile Route
@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        contact_details = request.form.get('contact_details')

        # Update profile details
        current_user.student_id = student_id
        current_user.contact_details = contact_details
        db.session.commit()
        flash('Profile updated successfully!', category='success')
    
    return render_template("profile.html", user=current_user)
