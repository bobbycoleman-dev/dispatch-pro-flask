from flask_app.extensions import db
from flask_login import UserMixin
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_app.models.dc_region import DCRegion


class User(UserMixin, db.Model):
    __tablename__ = "users"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    role = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    dc_id = Column(Integer, ForeignKey("distribution_centers.id"), nullable=False)
    user_dc = relationship("DistributionCenter", backref="users")

    region = ""
