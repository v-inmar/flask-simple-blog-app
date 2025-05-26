from app.extensions import db

def delete_post_service(post_obj):
    try:
        # Deleting for now
        # But it is probably best to have a is_deleted field in the database and just toggle that to true
        db.session.delete(post_obj)
        db.session.commit()
        return (True, "")
    except Exception:
        db.session.rollback()
        return (False, "")