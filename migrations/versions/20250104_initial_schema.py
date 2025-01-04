"""Initial database schema

Revision ID: 67daf4354321
Create Date: 2025-01-04 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67daf4354321'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=64), nullable=True),
        sa.Column('firstname', sa.String(length=64), nullable=True),
        sa.Column('lastname', sa.String(length=64), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')