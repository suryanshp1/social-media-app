"""add content column to posts table

Revision ID: 6d4b853c38d6
Revises: b7be349f6c1c
Create Date: 2023-02-11 09:43:38.994906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d4b853c38d6'
down_revision = 'b7be349f6c1c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
