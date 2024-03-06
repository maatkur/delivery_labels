"""create_users

Revision ID: 7a985059d84c
Revises: 
Create Date: 2023-10-16 16:14:20.804659

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a985059d84c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("code", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("password", sa.String(length=60), nullable=False),
        sa.Column("store", sa.String(length=3), nullable=True),
    )


def downgrade() -> None:
    op.drop_table(
        "users"
    )
