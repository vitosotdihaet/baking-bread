"""empty message

Revision ID: e6020703d830
Revises: 
Create Date: 2023-04-15 18:39:19.138746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6020703d830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('typeId', sa.Integer(), nullable=True))
        batch_op.drop_constraint('goods_good_type_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'good_types', ['typeId'], ['id'])
        batch_op.drop_column('good_type_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('good_type_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('goods_good_type_id_fkey', 'good_types', ['good_type_id'], ['id'])
        batch_op.drop_column('typeId')

    # ### end Alembic commands ###