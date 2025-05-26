from flask import render_template, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from ..forms.create_form import PostCreateForm # <-- repurposed the create form
from ..services.update_post_service import update_post_service
from ..services.read_post_service import read_post_service

@login_required
def update(pid):
    read_result = read_post_service(pid=pid)
    if read_result[0] == False:
        abort(500)
    if read_result[0] == None:
        abort(404)
    
    post_obj = read_result[1]
    if post_obj.author.id != current_user.id:
        abort(404)

    form = PostCreateForm() # <-- repurposed the create form
    if form.validate_on_submit():
        result = update_post_service(form=form, post_obj=post_obj)
        if result[0] == False:
            abort(500)
        
        flash(message="Post successfully updated!", category="info")
        return redirect(url_for("post.read", pid=pid))
    
    form.title.data = post_obj.title
    form.body.data = post_obj.body
    return render_template("update.html", form=form, pid=pid)