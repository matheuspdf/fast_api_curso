"""create updated_at column

Revision ID: 1e7d3e56ef88
Revises: 2a6475e80c83
Create Date: 2024-07-11 20:30:37.251437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01094866fabe'
down_revision: Union[str, None] = '2a6475e80c83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
