from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Address(db.Model, SerializerMixin):
    __tablename__ = "addresses"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    street = Column(String(45), nullable=False)
    city = Column(String(2), nullable=False)
    state = Column(String(45), nullable=False)
    zip_code = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    address_customer = relationship("Customer", backref="addresses")
