from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Driver(db.Model):
    __tablename__ = "drivers"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    license_type = Column(String(45), nullable=True)
    license_exp = Column(Date, nullable=True)
    dot_exp = Column(Date, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    dc_id = Column(Integer, ForeignKey("distribution_centers.id"), nullable=False)
    driver_dc = relationship("DistributionCenter", backref="drivers")
