"""empty message

Revision ID: 5c8c7dfdecbf
Revises: f0840ba1782e
Create Date: 2021-03-02 17:48:31.343049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c8c7dfdecbf'
down_revision = 'f0840ba1782e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('favorite', table_name='favorites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('favorite', 'favorites', ['favorite'], unique=True)
    # ### end Alembic commands ###