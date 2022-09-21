"""add user table

Revision ID: 42f286d0e528
Revises: 03a18ba8e990
Create Date: 2022-09-18 16:41:52.881781

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '42f286d0e528'
down_revision = '03a18ba8e990'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
