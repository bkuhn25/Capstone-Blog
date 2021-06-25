"""empty message

Revision ID: da23820324b5
Revises: 50b2102f2dfc
Create Date: 2021-06-25 06:54:12.061006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da23820324b5'
down_revision = '50b2102f2dfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_posts', 'test_field')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_posts', sa.Column('test_field', sa.VARCHAR(length=10), nullable=True))
    # ### end Alembic commands ###
