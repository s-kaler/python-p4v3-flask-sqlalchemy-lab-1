"""Initial migration.

Revision ID: 5febac2b593c
Revises: 
Create Date: 2024-10-18 03:51:37.873762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5febac2b593c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earthquakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earthquakes')
    # ### end Alembic commands ###
