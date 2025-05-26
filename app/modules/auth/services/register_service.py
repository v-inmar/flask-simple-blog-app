from app.modules.user.models import UserModel, UserPIDModel, UserTokenModel
from app.utils import generate_random_string
from app.extensions import db

def register_service(form):
    '''
    Returns tuple
    @param form - RegistrationForm
    '''
    try:
        user_obj = UserModel(firstname=str(form.firstname.data).strip(), lastname=str(form.lastname.data).strip(), email=str(form.email.data).strip().lower())
        user_obj.set_password(form.password.data)
        db.session.add(user_obj)
        db.session.flush()# flush into db so we can get an id

        # PID
        pid = ""
        while(True):
            pid = generate_random_string(min_length=8, max_length=16)
            pid_obj = UserPIDModel.query.filter_by(pid=pid).first()
            if pid_obj:
                continue
            else:
                break
        
        pid_obj = UserPIDModel(pid=pid, user_id=user_obj.id)
        db.session.add(pid_obj)
        db.session.flush()

        # Token
        token = ""
        while(True):
            token = generate_random_string(min_length=128, max_length=256)
            token_obj = UserTokenModel.query.filter_by(token=token).first()
            if token_obj:
                continue
            else:
                break
        
        token_obj = UserTokenModel(token=token, user_id=user_obj.id)
        db.session.add(token_obj)
        

        db.session.commit()
        return (user_obj, "")
    except Exception:

        db.session.rollback()
        return (False, "")