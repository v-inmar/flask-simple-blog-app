
from ..models.post_pid_model import PostPIDModel

def read_post_service(pid):
    try:
        pid_obj = PostPIDModel.query.filter_by(pid=pid).first()
        if pid_obj:
            if pid_obj.post:
                return (True, pid_obj.post)
        
        return (None, "")
    except Exception:
        return (False, "")