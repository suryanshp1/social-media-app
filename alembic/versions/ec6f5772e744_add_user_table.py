"""add user table

Revision ID: ec6f5772e744
Revises: 6d4b853c38d6
Create Date: 2023-02-11 09:50:47.954936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec6f5772e744'
down_revision = '6d4b853c38d6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), nullable=False), sa.Column("email", sa.String(), nullable=False), sa.Column("password", sa.String(), nullable=False), sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
