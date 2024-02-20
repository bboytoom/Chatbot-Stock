"""first migration

Revision ID: 118611f9d4b6
Revises: 
Create Date: 2024-02-20 03:48:50.138362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '118611f9d4b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock_symbol',
    sa.Column('uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('symbol_name', sa.String(length=50), nullable=True),
    sa.Column('symbol', sa.String(length=20), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    with op.batch_alter_table('stock_symbol', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_stock_symbol_symbol'), ['symbol'], unique=False)
        batch_op.create_index(batch_op.f('ix_stock_symbol_uuid'), ['uuid'], unique=True)

    op.create_table('users',
    sa.Column('uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=70), nullable=False),
    sa.Column('birth_day', sa.Date(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_uuid'), ['uuid'], unique=True)

    op.create_table('historical_stock_price',
    sa.Column('uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('stock_symbol_uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('open_price', sa.Float(precision=4, asdecimal=3), nullable=True),
    sa.Column('high_price', sa.Float(precision=4, asdecimal=3), nullable=True),
    sa.Column('low_price', sa.Float(precision=4, asdecimal=3), nullable=True),
    sa.Column('close_price', sa.Float(precision=4, asdecimal=3), nullable=True),
    sa.Column('date_stock', sa.Date(), nullable=False),
    sa.Column('time_stock', sa.Time(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['stock_symbol_uuid'], ['stock_symbol.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid')
    )
    with op.batch_alter_table('historical_stock_price', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_historical_stock_price_date_stock'), ['date_stock'], unique=False)
        batch_op.create_index(batch_op.f('ix_historical_stock_price_stock_symbol_uuid'), ['stock_symbol_uuid'], unique=False)
        batch_op.create_index(batch_op.f('ix_historical_stock_price_uuid'), ['uuid'], unique=True)
        batch_op.create_index('ix_stock_symbol_date_stock', ['stock_symbol_uuid', 'date_stock'], unique=False)

    op.create_table('user_stock_symbol',
    sa.Column('uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('user_uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('stock_symbol_uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['stock_symbol_uuid'], ['stock_symbol.uuid'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('user_uuid', 'stock_symbol_uuid', name='uq_user_stock_symbol')
    )
    with op.batch_alter_table('user_stock_symbol', schema=None) as batch_op:
        batch_op.create_index('ix_user_stock_symbol', ['user_uuid', 'stock_symbol_uuid'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_stock_symbol_stock_symbol_uuid'), ['stock_symbol_uuid'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_stock_symbol_user_uuid'), ['user_uuid'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_stock_symbol_uuid'), ['uuid'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_stock_symbol', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_stock_symbol_uuid'))
        batch_op.drop_index(batch_op.f('ix_user_stock_symbol_user_uuid'))
        batch_op.drop_index(batch_op.f('ix_user_stock_symbol_stock_symbol_uuid'))
        batch_op.drop_index('ix_user_stock_symbol')

    op.drop_table('user_stock_symbol')
    with op.batch_alter_table('historical_stock_price', schema=None) as batch_op:
        batch_op.drop_index('ix_stock_symbol_date_stock')
        batch_op.drop_index(batch_op.f('ix_historical_stock_price_uuid'))
        batch_op.drop_index(batch_op.f('ix_historical_stock_price_stock_symbol_uuid'))
        batch_op.drop_index(batch_op.f('ix_historical_stock_price_date_stock'))

    op.drop_table('historical_stock_price')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_uuid'))

    op.drop_table('users')
    with op.batch_alter_table('stock_symbol', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_stock_symbol_uuid'))
        batch_op.drop_index(batch_op.f('ix_stock_symbol_symbol'))

    op.drop_table('stock_symbol')
    # ### end Alembic commands ###
