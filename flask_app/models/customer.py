from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    company_name = Column(String(45), nullable=False)
    poc_first_name = Column(String(45), nullable=False)
    poc_last_name = Column(String(45), nullable=False)
    poc_number = Column(String(45), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    dc_id = Column(Integer, ForeignKey("distribution_centers.id"), nullable=False)
    customer_dc = relationship("DistributionCenter", backref="customers")
