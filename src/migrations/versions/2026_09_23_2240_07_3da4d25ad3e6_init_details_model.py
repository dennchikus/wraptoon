"""Init details model

Revision ID: 3da4d25ad3e6
Revises:
Create Date: 2026-09-23 22:40:07.983957

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "3da4d25ad3e6"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "details",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name_detail", sa.String(length=40), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("details")
