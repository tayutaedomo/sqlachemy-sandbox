"""add comments table

Revision ID: 003
Revises: 002
Create Date: 2021-08-15 23:10:50.908345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=255), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('book_id', mysql.INTEGER(display_width=11), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_book_id'), 'comments', ['book_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_book_id'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###
