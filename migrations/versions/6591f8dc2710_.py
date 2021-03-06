"""empty message

Revision ID: 6591f8dc2710
Revises: 
Create Date: 2020-12-30 23:04:43.851421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6591f8dc2710'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publishers', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('publishers', sa.Column('pioneer', sa.Boolean(), nullable=True))
    op.add_column('publishers', sa.Column('privilege', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publishers', 'privilege')
    op.drop_column('publishers', 'pioneer')
    op.drop_column('publishers', 'gender')
    # ### end Alembic commands ###
