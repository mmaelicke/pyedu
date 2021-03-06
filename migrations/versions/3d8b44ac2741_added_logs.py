"""added logs

Revision ID: 3d8b44ac2741
Revises: 2f94625a0289
Create Date: 2017-07-04 08:10:03.234678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d8b44ac2741'
down_revision = '2f94625a0289'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logs',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('tstamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'task_id', 'tstamp')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logs')
    ### end Alembic commands ###
