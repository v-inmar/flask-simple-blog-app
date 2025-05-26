from ..models.user_pid_model import UserPIDModel

def profile_service(pid):
    try:
        pid_obj = UserPIDModel.query.filter_by(pid=pid).first()
        if pid_obj:
            return (True, pid_obj.user)
        return (None, "")
    except Exception:
        return (False, "")