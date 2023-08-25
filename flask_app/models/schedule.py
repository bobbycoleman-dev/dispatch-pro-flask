from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Date, Boolean
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Schedule(db.Model, SerializerMixin):
    __tablename__ = "schedules"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    start_date = Column(Date(), nullable=False)
    first_run_stops = Column(Integer(), default=4)
    has_second_runs = Column(Integer(), default=1)
    second_run_stops = Column(Integer, default=3)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    dc_id = Column(Integer, ForeignKey("distribution_centers.id"), nullable=False)
    truck_id = Column(Integer, ForeignKey("trucks.id"), nullable=False)
    truck = relationship("Truck", backref="schedules")
