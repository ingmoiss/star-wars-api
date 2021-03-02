"""empty message

Revision ID: f0840ba1782e
Revises: 
Create Date: 2021-03-02 17:15:31.566312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0840ba1782e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('birth', sa.String(length=300), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('skin_color', sa.String(length=300), nullable=False),
    sa.Column('eye_color', sa.String(length=300), nullable=False),
    sa.Column('hair_color', sa.String(length=300), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('edited', sa.String(length=300), nullable=False),
    sa.Column('created', sa.String(length=300), nullable=False),
    sa.Column('url', sa.String(length=300), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.PrimaryKeyConstraint('character_id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('planet',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.String(length=300), nullable=False),
    sa.Column('terrain', sa.String(length=300), nullable=False),
    sa.Column('surface_water', sa.Integer(), nullable=False),
    sa.Column('created', sa.String(length=300), nullable=False),
    sa.Column('edited', sa.String(length=300), nullable=False),
    sa.Column('url', sa.String(length=300), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.PrimaryKeyConstraint('planet_id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=300), nullable=False),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.Column('email', sa.String(length=300), nullable=False),
    sa.Column('first_name', sa.String(length=300), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('favorites',
    sa.Column('fav_id', sa.Integer(), nullable=False),
    sa.Column('favorite', sa.String(length=300), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('fav_id'),
    sa.UniqueConstraint('favorite')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###