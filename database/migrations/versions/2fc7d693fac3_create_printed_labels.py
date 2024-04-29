"""create_printed_labels

Revision ID: 2fc7d693fac3
Revises: 6f820511a4f7
Create Date: 2024-04-24 10:13:01.111617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fc7d693fac3'
down_revision: Union[str, None] = '6f820511a4f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "printed_labels",
        sa.Column("order_number", sa.Integer()),
        sa.Column("checker", sa.Integer(), nullable=False),
        sa.Column("volumes", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date, nullable=False, server_default=sa.func.now()),
        sa.Column("reprinted", sa.Boolean, server_default=sa.false()),
        sa.Column("reason", sa.String(length=100), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("printed_labels")
