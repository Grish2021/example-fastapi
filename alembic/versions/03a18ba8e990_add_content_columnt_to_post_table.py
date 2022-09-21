"""add content columnt to post table

Revision ID: 03a18ba8e990
Revises: edecf2a7309a
Create Date: 2022-09-16 22:11:28.694654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03a18ba8e990'
down_revision = 'edecf2a7309a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),  nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
