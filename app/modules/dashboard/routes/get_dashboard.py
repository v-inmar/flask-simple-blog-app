from flask import render_template, url_for
from flask_login import current_user, login_required

@login_required
def get_dashboard():
    posts = []
    if len(current_user.posts) > 0:
        for post in current_user.posts:
            posts.append({
                "title": post.title,
                "datetime": post.datetime_created,
                "url": url_for("post.read", pid=post.post_pid.pid)
            })

    return render_template("get_dashboard.html", posts=posts)