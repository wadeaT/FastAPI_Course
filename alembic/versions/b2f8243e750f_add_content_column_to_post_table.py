"""add content column to post table

Revision ID: b2f8243e750f
Revises: f937b305ab80
Create Date: 2026-09-25 19:00:37.944560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2f8243e750f'
down_revision: Union[str, Sequence[str], None] = 'f937b305ab80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
