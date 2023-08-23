from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Truck(db.Model):
    __tablename__ = "trucks"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    number = Column(String(45), nullable=False)
    make = Column(String(45), nullable=True)
    model = Column(String(45), nullable=True)
    year = Column(String(45), nullable=True)
    vin = Column(String(45), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    dc_id = Column(Integer, ForeignKey("distribution_centers.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    truck_dc = relationship("DistributionCenter", backref="trucks")
    truck_driver = relationship("Driver", backref="trucks")
