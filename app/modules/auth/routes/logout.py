from flask import redirect, url_for, flash
from flask_login import logout_user, login_required

@login_required
def logout():
    '''
    Route for logging out a user
    '''
    logout_user()
    flash(message="You have been logged out.", category="info")
    return redirect(url_for("auth.login"))