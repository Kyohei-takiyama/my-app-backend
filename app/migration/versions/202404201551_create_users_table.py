"""create users table

Revision ID: c79e44a1498e
Revises:
Create Date: 2024-04-20 15:51:48.628639+09:00

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c79e44a1498e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("login_id", sa.String(50), nullable=False),
        sa.Column("password", sa.Text(), nullable=False),
    )


def downgrade():
    op.drop_table("users")
