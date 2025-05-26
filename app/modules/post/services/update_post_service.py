from app.extensions import db

def update_post_service(form, post_obj):
    try:
        post_obj.title = str(form.title.data).strip()
        post_obj.body = str(form.body.data).strip()
        db.session.commit()
        return (True, post_obj)
    except Exception:
        db.session.rollback()
        return (False, "")