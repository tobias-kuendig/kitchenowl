"""add photo to item

Revision ID: d02c6d84483f
Revises: bd383e73ef4d
Create Date: 2026-02-05 20:29:14.668945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02c6d84483f'
down_revision = 'bd383e73ef4d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('item', sa.Column('photo', sa.String(), nullable=True))

def downgrade():
    op.drop_column('item', 'photo')
