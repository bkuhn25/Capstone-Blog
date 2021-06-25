"""empty message

Revision ID: 50b2102f2dfc
Revises: 5580b8259e0e
Create Date: 2021-06-25 06:47:46.103048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50b2102f2dfc'
down_revision = '5580b8259e0e'
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
