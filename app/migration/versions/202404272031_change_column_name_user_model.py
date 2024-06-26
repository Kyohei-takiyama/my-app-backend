"""change column name User model

Revision ID: 756e2ca1dc83
Revises: e2288bb16297
Create Date: 2024-04-27 20:31:41.539087+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '756e2ca1dc83'
down_revision = 'e2288bb16297'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=50), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
