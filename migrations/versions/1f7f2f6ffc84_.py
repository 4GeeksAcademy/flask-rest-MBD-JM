"""empty message

Revision ID: 1f7f2f6ffc84
Revises: 583e86901557
Create Date: 2025-04-13 16:46:39.366158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f7f2f6ffc84'
down_revision = '583e86901557'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint('comment_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('post_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'post', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('post_user_id_fkey', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('comment_user_id_fkey', 'post', ['user_id'], ['id'])

    # ### end Alembic commands ###
