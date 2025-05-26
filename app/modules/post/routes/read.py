from flask import render_template, abort, url_for
from flask_login import current_user, login_required


from ..services.read_post_service import read_post_service

@login_required
def read(pid):

    result = read_post_service(pid)
    if result[0] ==  False:
        abort(500)
    
    if result[0] == None:
        abort(404)
    
    post_obj = result[1]

    post = {
        "title": post_obj.title,
        "body": post_obj.body,
        "datetime": post_obj.datetime_created,
        "author": {
            "name": post_obj.author.firstname + " " + post_obj.author.lastname,
            "is_current_user": False,
            "link": url_for("user.profile", pid=post_obj.author.user_pid.pid), # <--- change this to user profile link
        },
        "update_link": url_for("post.update", pid=pid),
        "delete_link": url_for("post.delete", pid=pid)
    }


    if current_user.is_authenticated:
        if post_obj.author.id == current_user.id:
            post['author']['is_current_user'] = True
    return render_template("read.html", post=post)