"""empty message

Revision ID: d4a3042c9508
Revises: 75189beb211f
Create Date: 2020-03-10 12:21:13.553000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4a3042c9508'
down_revision = '75189beb211f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('international_universities', sa.Column('link', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('international_universities', 'link')
    # ### end Alembic commands ###
