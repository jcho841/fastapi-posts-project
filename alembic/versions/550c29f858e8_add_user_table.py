"""add user table

Revision ID: 550c29f858e8
Revises: a024da699e81
Create Date: 2022-01-18 17:31:21.651098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '550c29f858e8'
down_revision = 'a024da699e81'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
