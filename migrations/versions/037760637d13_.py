"""empty message

Revision ID: 037760637d13
Revises: 
Create Date: 2019-01-05 19:51:08.815314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '037760637d13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('isbn', sa.Integer(), nullable=True),
    sa.Column('authors_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['authors_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('authors')
    # ### end Alembic commands ###
