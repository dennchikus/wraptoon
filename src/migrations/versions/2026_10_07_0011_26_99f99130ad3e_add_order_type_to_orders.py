"""add order_type to orders

Revision ID: 99f99130ad3e
Revises: 952178c0d580
Create Date: 2026-10-07 00:11:26.654757

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "99f99130ad3e"
down_revision: Union[str, Sequence[str], None] = "952178c0d580"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "orders", sa.Column("order_type", sa.String(length=15), nullable=False)
    )
    op.alter_column("orders", "price", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "orders",
        "ids_service_details",
        existing_type=sa.VARCHAR(length=100),
        nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "orders",
        "ids_service_details",
        existing_type=sa.VARCHAR(length=100),
        nullable=False,
    )
    op.alter_column("orders", "price", existing_type=sa.INTEGER(), nullable=False)
    op.drop_column("orders", "order_type")
