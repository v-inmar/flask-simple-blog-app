from app.abstract_base_model import AbstractBaseModel
from app.extensions import db



class UserPIDModel(AbstractBaseModel): # correspond to /users/<pid>
    __tablename__ = "user_pid"
    pid = db.Column(db.String(256), unique=True, nullable=False)

    # 1 user can only have 1 unique pid
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"), nullable=False, unique=True)

    # Back reference to User (this allows you to access the User object from User PID)
    user = db.relationship('UserModel', back_populates='user_pid')
