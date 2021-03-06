"""empty message

Revision ID: 5618a28b9237
Revises: 558df7bfb739
Create Date: 2018-08-02 20:34:21.034912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5618a28b9237'
down_revision = '558df7bfb739'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=23), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('path', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_title'), 'course', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_course_title'), table_name='course')
    op.drop_table('course')
    # ### end Alembic commands ###
