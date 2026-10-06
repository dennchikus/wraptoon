"""add orders table

Revision ID: 952178c0d580
Revises: 0575191553e8
Create Date: 2026-10-06 23:24:34.342824

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "952178c0d580"
down_revision: Union[str, Sequence[str], None] = "0575191553e8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("client_name", sa.String(length=50), nullable=False),
        sa.Column("client_number", sa.String(length=20), nullable=False),
        sa.Column("client_car", sa.String(length=50), nullable=False),
        sa.Column("client_comment", sa.String(length=500), nullable=True),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("ids_service_details", sa.String(length=100), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("orders")
