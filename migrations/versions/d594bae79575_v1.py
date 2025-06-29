"""v1

Revision ID: d594bae79575
Revises: 
Create Date: 2025-06-23 15:15:50.074009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd594bae79575'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_action_name'), 'action', ['name'], unique=False)
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_menu_name'), 'menu', ['name'], unique=False)
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('websites', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organization_name'), 'organization', ['name'], unique=False)
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('otp', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.Column('super', sa.Boolean(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_userinfo_email'), 'userinfo', ['email'], unique=False)
    op.create_table('userorglink',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['org_id'], ['organization.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['userinfo.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'org_id')
    )
    # ### end Alembic commands ###

def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userorglink')
    op.drop_index(op.f('ix_userinfo_email'), table_name='userinfo')
    op.drop_table('userinfo')
    op.drop_index(op.f('ix_organization_name'), table_name='organization')
    op.drop_table('organization')
    op.drop_index(op.f('ix_menu_name'), table_name='menu')
    op.drop_table('menu')
    op.drop_index(op.f('ix_action_name'), table_name='action')
    op.drop_table('action')
    # ### end Alembic commands ###
