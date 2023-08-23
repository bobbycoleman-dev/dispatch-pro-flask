from flask_app.extensions import db
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class DistributionCenter(db.Model):
    __tablename__ = "distribution_centers"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    nickname = Column(String(45), nullable=False)
    street = Column(String(45), nullable=False, unique=True)
    city = Column(String(45), nullable=False, unique=True)
    state = Column(String(45), nullable=False, unique=True)
    zip_code = Column(String(45), nullable=False, unique=True)
    region = Column(String(45), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
