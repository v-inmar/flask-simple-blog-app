from app.abstract_base_model import AbstractBaseModel
from app.extensions import db

class UserTokenModel(AbstractBaseModel): # token used for session and not user sensitive info
    __tablename__ = "user_token"
    token = db.Column(db.String(256), unique=True, nullable=False)

    # 1 user can only have 1 unique token
    # nullable because user is allowed to change token thus making the token owned by nobody
    # tokens are not deleted straight away - maybe few months when performing cleanup
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"), nullable=True, unique=True)


    # Back reference to User (this allows you to access the User object from User Token)
    user = db.relationship('UserModel', back_populates='user_token')
