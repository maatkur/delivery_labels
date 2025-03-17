"""initial_migrations

Revision ID: 8c0d1c442352
Revises: 
Create Date: 2024-12-27 09:31:16.570944
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c0d1c442352'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criação das tabelas
    op.create_table('permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('password', sa.String(length=60), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_permissions',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['permission_id'], ['permissions.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('user_id', 'permission_id')
    )

    # Inserção dos dados padrões com bulk_insert
    op.bulk_insert(
        sa.table('users',
                 sa.column('id'),
                 sa.column('name'),
                 sa.column('password')),
        [
            {
                'id': 999,
                'name': 'admin',
                'password': '$2b$12$Rkp1IqxpdObvyT4UPg8WDeELbeRUskusZXfzv5JkYePb.KZsttqc.'
            }
        ]
    )

    op.bulk_insert(
        sa.table('permissions',
                 sa.column('id'),  # ID será gerado automaticamente
                 sa.column('description')),
        [
            {'description': 'MANAGE USERS'},
            {'description': 'REPORT'},
            {'description': 'REPRINT LABELS'}
        ]
    )

    # Como as permissões têm IDs autoincrement, assumimos que começam em 1, 2, 3
    op.bulk_insert(
        sa.table('users_permissions',
                 sa.column('user_id'),
                 sa.column('permission_id')),
        [
            {'user_id': 999, 'permission_id': 1},  # MANAGE USERS
            {'user_id': 999, 'permission_id': 2},  # REPORT
            {'user_id': 999, 'permission_id': 3}   # REPRINT LABELS
        ]
    )


def downgrade() -> None:
    op.drop_table('users_permissions')
    op.drop_table('users')
    op.drop_table('permissions')
