"""add content to post tables

Revision ID: a024da699e81
Revises: 8dc1ececfd66
Create Date: 2022-01-18 17:26:20.820772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a024da699e81'
down_revision = '8dc1ececfd66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
