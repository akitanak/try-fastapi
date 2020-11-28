"""create Task table

Revision ID: 5866d222a2e3
Revises: 
Create Date: 2020-11-28 14:54:37.538493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5866d222a2e3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tasks",
        sa.Column("id", sa.String(length=36)),
        sa.Column("task_name", sa.String(length=32), nullable=False),
        sa.Column("due_data", sa.Date(), nullable=True),
        sa.Column("priority", sa.String(8), nullable=True),
        sa.Column("is_done", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("tasks")
