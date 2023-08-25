from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Date
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Delivery(db.Model, SerializerMixin):
    __tablename__ = "deliveries"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    is_first_run = Column(Integer(), nullable=False)
    stop_num = Column(Integer(), nullable=False)
    date = Column(Date(), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    schedule_id = Column(Integer, ForeignKey("schedules.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    dc_id = Column(Integer, ForeignKey("distribution_centers.id"), nullable=False)
    customer = relationship("Customer", backref="deliveries")
    # schedule = relationship("Schedule", backref="deliveries")
    address = relationship("Address", backref="deliveries")
    serialize_only = (
        "customer.company_name",
        "address.city",
        "is_first_run",
        "stop_num",
        "schedule_id",
    )
    serialize_rules = ()
