"""add user table

Revision ID: 8742716318fd
Revises: b2f8243e750f
Create Date: 2026-09-25 19:05:16.956878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8742716318fd'
down_revision: Union[str, Sequence[str], None] = 'b2f8243e750f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id',sa.Integer(), nullable=False),
                    sa.Column('email',sa.String(), nullable=False),
                    sa.Column('password', sa.String(),nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                               server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users')
    pass
