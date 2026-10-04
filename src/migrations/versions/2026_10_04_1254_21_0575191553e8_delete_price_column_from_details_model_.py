"""delete price column from details model and schemas and rename service name column

Revision ID: 0575191553e8
Revises: 138359667e27
Create Date: 2026-10-04 12:54:21.086743

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "0575191553e8"
down_revision: Union[str, Sequence[str], None] = "138359667e27"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("details", "price")
    op.alter_column("services", "name", new_column_name="name_service")


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("services", "name_service", new_column_name="name")
    op.add_column(
        "details", sa.Column("price", sa.INTEGER(), autoincrement=False, nullable=False)
    )
