from flask_login import current_user
from ..models.post_model import PostModel
from ..models.post_pid_model import PostPIDModel
from app.extensions import db
from app.utils import generate_random_string

def create_post_service(form, user_id):
    try:
        post_obj = PostModel(title=str(form.title.data).strip(), body=form.body.data, user_id=user_id)
        db.session.add(post_obj)
        db.session.flush()

        pid = ""
        while(True):
            pid = generate_random_string(min_length=16, max_length=32)
            pid_obj = PostPIDModel.query.filter_by(pid=pid).first()
            if pid_obj:
                continue
            else:
                break
        
        pid_obj = PostPIDModel(pid=pid, post_id=post_obj.id)
        db.session.add(pid_obj)
        
        db.session.commit()
        return (True, post_obj)
    except Exception:
        db.session.rollback()
        return (False, "")