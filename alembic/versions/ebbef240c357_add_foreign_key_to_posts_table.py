"""add foreign-key to posts table

Revision ID: ebbef240c357
Revises: b7eb9cb5275b
Create Date: 2023-02-21 08:39:20.006068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebbef240c357'
down_revision = 'b7eb9cb5275b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', 
                            local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('poss_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
