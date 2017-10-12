"""empty message

Revision ID: 7a32290934da
Revises: 
Create Date: 2017-10-12 01:10:10.859989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a32290934da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('max_visits', sa.Integer(), nullable=True),
    sa.Column('visits_count', sa.Integer(), nullable=True),
    sa.Column('payload', sa.Binary(), nullable=False),
    sa.Column('expiration_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    # ### end Alembic commands ###