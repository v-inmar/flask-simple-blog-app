from app.abstract_base_model import AbstractBaseModel
from app.extensions import db



class PostPIDModel(AbstractBaseModel): # correspond to /users/<pid>
    __tablename__ = "post_pid"
    pid = db.Column(db.String(256), unique=True, nullable=False)

    # 1 post can only have 1 unique pid
    # Nullable because we can delete a post without having to delete the pid yet
    # Maybe delete this pid after few months or never.
    # This is to avoid another pid potentially pointing to a different post just
    # because the post has already been delete
    post_id = db.Column(db.BigInteger, db.ForeignKey("post.id"), nullable=True, unique=True)

    # Back reference to Post (this allows you to access the Post object from Post PID)
    post = db.relationship('PostModel', back_populates='post_pid')
