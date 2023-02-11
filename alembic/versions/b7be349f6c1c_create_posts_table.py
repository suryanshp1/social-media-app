"""create posts table

Revision ID: b7be349f6c1c
Revises: 
Create Date: 2022-12-04 18:59:00.965583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7be349f6c1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
