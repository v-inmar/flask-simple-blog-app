from app.modules.user.models.user_model import UserModel

def login_service(form):
    '''
    Returns tuple 
    @param form: LoginForm
    '''
    try:
        email_data = form.email.data
        user_obj = UserModel.query.filter_by(email=email_data).first()
        if user_obj:
            if user_obj.check_password(form.password.data):
                return (user_obj, "")
        form.email.errors.append("Invalid email address and/or password")
        form.password.errors.append("Invalid email address and/or password")
        return (None, form)
    except Exception:
        return (False, "")