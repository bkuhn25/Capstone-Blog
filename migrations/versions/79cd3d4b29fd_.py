"""empty message

Revision ID: 79cd3d4b29fd
Revises: 
Create Date: 2021-06-24 18:52:35.699198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79cd3d4b29fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_posts', sa.Column('test_field', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_posts', 'test_field')
    # ### end Alembic commands ###
