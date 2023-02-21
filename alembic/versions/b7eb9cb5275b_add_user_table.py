"""add user table

Revision ID: b7eb9cb5275b
Revises: 247367dfc625
Create Date: 2023-02-21 08:17:11.253255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7eb9cb5275b'
down_revision = '247367dfc625'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False),
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email')
    )
    pass

def downgrade():
    op.drop_table('users')
    pass
