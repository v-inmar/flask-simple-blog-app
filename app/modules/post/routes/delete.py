from flask import abort, url_for, redirect, flash
from flask_login import current_user, login_required
from ..services.read_post_service import read_post_service
from ..services.delete_post_service import delete_post_service

@login_required
def delete(pid):
    read_result = read_post_service(pid)
    if read_result[0] ==  False:
        abort(500)
    
    if read_result[0] == None:
        abort(404)

    if current_user.id != read_result[1].author.id:
        abort(404)
    


    result = delete_post_service(post_obj=read_result[1])
    if result[0] == False:
        abort(500)

    flash(message="Post successfully deleted!", category="info")
    # Delete route doesn't have a template. It is just a link
    # just like the logout feature
    return redirect(url_for("dashboard.dashboard"))