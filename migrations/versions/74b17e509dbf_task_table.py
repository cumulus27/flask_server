"""task table

Revision ID: 74b17e509dbf
Revises: 
Create Date: 2019-03-16 15:37:41.457533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74b17e509dbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
