"""add role user

Revision ID: 02984d98016d
Revises: 3da9073508ea
Create Date: 2024-09-15 07:54:30.916406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02984d98016d'
down_revision: Union[str, None] = '3da9073508ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('role', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)


def downgrade() -> None:
    pass
