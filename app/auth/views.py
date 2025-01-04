from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from .oauth import OAuthSignIn

@auth.route('/login')  # Make sure this route exists
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@auth.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@auth.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    
    oauth = OAuthSignIn.get_provider(provider)
    email, firstname, lastname = oauth.callback()
    
    if email is None:
        flash('Authentication failed.', 'danger')
        return redirect(url_for('auth.login'))
    
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email,
                   firstname=firstname,
                   lastname=lastname)
        db.session.add(user)
        db.session.commit()
    
    login_user(user, True)
    flash('Successfully logged in!', 'success')
    return redirect(url_for('main.index'))
