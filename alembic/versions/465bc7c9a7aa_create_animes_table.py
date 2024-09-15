"""create animes table

Revision ID: 465bc7c9a7aa
Revises: 
Create Date: 2024-09-15 06:31:07.520982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '465bc7c9a7aa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('rating', sa.Double(), nullable=True),
    sa.Column('episodes', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('genre', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animes_description'), 'animes', ['description'], unique=False)
    op.create_index(op.f('ix_animes_id'), 'animes', ['id'], unique=False)
    op.create_index(op.f('ix_animes_title'), 'animes', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_animes_title'), table_name='animes')
    op.drop_index(op.f('ix_animes_id'), table_name='animes')
    op.drop_index(op.f('ix_animes_description'), table_name='animes')
    op.drop_table('animes')
    # ### end Alembic commands ###
