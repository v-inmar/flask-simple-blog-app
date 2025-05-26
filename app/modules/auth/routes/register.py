from flask import render_template, abort, redirect, url_for, flash
from flask_login import login_user
from ..forms.register_form import RegisterForm
from ..services.register_service import register_service
from app.utils import must_not_be_authed

@must_not_be_authed
def register():
    '''
    Route for registering a user
    '''
    form = RegisterForm()
    if form.validate_on_submit():
        result = register_service(form=form)
        if result[0] == False:
            abort(500)
        login_user(result[0], remember=True)
        flash(message="Welcome to the blog website.", category="info")
        return redirect(url_for('dashboard.dashboard'))
    return render_template("register.html", form=form)