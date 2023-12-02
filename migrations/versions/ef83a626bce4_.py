"""empty message

Revision ID: ef83a626bce4
Revises: 
Create Date: 2023-11-28 21:26:48.484895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef83a626bce4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_table',
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=126), nullable=False),
    sa.Column('specialty', sa.String(length=32), nullable=False),
    sa.Column('working_area', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('dashboards_table',
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickets_table',
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('status', sa.String(length=32), nullable=False),
    sa.Column('dashboard_id', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['dashboard_id'], ['dashboards_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tickets_table')
    op.drop_table('dashboards_table')
    op.drop_table('users_table')
    # ### end Alembic commands ###