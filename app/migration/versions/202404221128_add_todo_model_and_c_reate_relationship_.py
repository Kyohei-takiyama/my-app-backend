"""add todo model and c
reate relationship user and todos

Revision ID: e2288bb16297
Revises: d6b7efc36e7b
Create Date: 2024-04-22 11:28:19.987719+09:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e2288bb16297'
down_revision = 'd6b7efc36e7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('todo_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('tags', sa.Text(), nullable=False),
    sa.Column('is_archived', sa.Boolean(), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('todo_id')
    )
    op.create_index(op.f('ix_todos_todo_id'), 'todos', ['todo_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todos_todo_id'), table_name='todos')
    op.drop_table('todos')
    # ### end Alembic commands ###