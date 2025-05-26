from flask import render_template, redirect, url_for, abort, flash, request
from flask_login import login_user
from app.utils import must_not_be_authed
from ..forms.login_form import LoginForm
from ..services.login_service import login_service

@must_not_be_authed
def login():
    '''
    Route for logging in a user
    '''
    form = LoginForm()
    if form.validate_on_submit():
        result = login_service(form=form)
        if result[0] == False:
            abort(code=500)
        if result[0] == None:
            form = result[1]
        else:
            login_user(result[0], remember=form.remember_me.data) # Log the user in
            flash(message="Welcome back!", category="info")
            # or just return to the dashboard
            next_page = request.args.get('next')
            return redirect(next_page or url_for("dashboard.dashboard"))
    return render_template("login.html", form=form)