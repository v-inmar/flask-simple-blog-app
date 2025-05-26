from app.extensions import db
from sqlalchemy.sql import func

class AbstractBaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.BigInteger, primary_key=True)
    datetime_created = db.Column(db.DateTime, default=func.now()) # func.now() genertes current utc time for each row creation