"""add role user

Revision ID: 3da9073508ea
Revises: 659c40a94d83
Create Date: 2024-09-15 07:51:22.312405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da9073508ea'
down_revision: Union[str, None] = '659c40a94d83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('role', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_animes_poster'), 'users', ['role'], unique=False)


def downgrade() -> None:
    pass
