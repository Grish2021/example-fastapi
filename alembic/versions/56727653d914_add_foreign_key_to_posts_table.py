"""add foreign-key to posts table

Revision ID: 56727653d914
Revises: 42f286d0e528
Create Date: 2022-09-18 17:11:57.214095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56727653d914'
down_revision = '42f286d0e528'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
