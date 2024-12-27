from sqlalchemy import Table, Column, Integer, ForeignKey
from database.base import Base

users_permissions = Table(
    "users_permissions",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True),
)
