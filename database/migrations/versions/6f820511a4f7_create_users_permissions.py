"""create_users_permissions

Revision ID: 6f820511a4f7
Revises: c75b39cf4e28
Create Date: 2023-11-07 11:34:40.850896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f820511a4f7'
down_revision: Union[str, None] = '7a985059d84c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users_permissions',
        sa.Column('code', sa.Integer, sa.ForeignKey('users.code'), primary_key=True),
        sa.Column('admin', sa.Boolean, server_default=sa.false()),
        sa.Column('reprint', sa.Boolean, server_default=sa.false()),
        sa.Column('report_access', sa.Boolean, server_default=sa.false()),
    )


def downgrade() -> None:
    op.drop_table(
        'users_permissions'
    )
