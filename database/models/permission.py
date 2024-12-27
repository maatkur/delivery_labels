from datetime import datetime
import pytz
from sqlalchemy import Column, Integer, String, func, DateTime
from sqlalchemy.orm import relationship
from database.base import Base
from database.models.user_permission import users_permissions


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    description = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')), onupdate=func.now())

    users = relationship("User", secondary=users_permissions, back_populates="permissions")
