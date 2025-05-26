from app.abstract_base_model import AbstractBaseModel
from app.extensions import db

class PostModel(AbstractBaseModel):
    __tablename__ = "post"
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    # One-to-one relationship with Post PID
    post_pid = db.relationship('PostPIDModel', back_populates='post', uselist=False)
