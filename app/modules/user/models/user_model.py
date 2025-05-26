from app.abstract_base_model import AbstractBaseModel
from app.extensions import db
from flask_login import UserMixin
import bcrypt

# Note: All fields here can be move to their own model to avoid duplication i.e. firstname and lastname
# this is just for simplicity
class UserModel(AbstractBaseModel, UserMixin):
    __tablename__ = "user"
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False) # hashed value

    # One-to-one relationship with User PID
    user_pid = db.relationship('UserPIDModel', back_populates='user', uselist=False)
    # One-to-one relationship with User Token
    user_token = db.relationship('UserTokenModel', back_populates='user', uselist=False)

    # One-to-many relationship with Post
    posts = db.relationship('PostModel', backref='author', lazy=True, order_by='PostModel.datetime_created.desc()') 

    def set_password(self, new_password):
        # encoded to utf8 so it accepts variety of non-romanized characters
        self.password = bcrypt.hashpw(password=str(new_password).encode("utf8"), salt=bcrypt.gensalt())

    def check_password(self, password):
        # encoded to utf8 so it accepts variety of non-romanized characters
        return bcrypt.checkpw(password=str(password).encode("utf8"), hashed_password=str(self.password).encode("utf8"))
    
    # Since we are using alternative token for the login_manager.user_loader
    # we need to override the UserMixin's get_id() with the one below
    # to make it get the actual token
    def get_id(self):
        return self.user_token.token or None

    







