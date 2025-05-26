from flask import render_template, url_for, abort
from flask_login import current_user, login_required
from ..services.profile_service import profile_service

@login_required
def profile(pid):
    result = profile_service(pid=pid)
    if result[0] == False:
        abort(500)

    if result[0] ==  None:
        abort(404)
    

    post_objs = result[1].posts

    user = {
        "name": result[1].firstname + " " + result[1].lastname,
        "posts":[]
    }

    if post_objs:
        for post in post_objs:
            p = {
                "title": post.title,
                "datetime": post.datetime_created,
                "url": url_for("post.read", pid=post.post_pid.pid)
            }
            user['posts'].append(p)

    return render_template("profile.html", user=user)